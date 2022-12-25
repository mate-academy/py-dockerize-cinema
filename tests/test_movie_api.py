import tempfile
import os

from PIL import Image
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

from cinema.models import Movie, MovieSession, CinemaHall, Genre, Actor
from cinema.serializers import MovieListSerializer, MovieDetailSerializer

MOVIE_URL = reverse("cinema:movie-list")
MOVIE_SESSION_URL = reverse("cinema:moviesession-list")


def sample_movie(**params):
    defaults = {
        "title": "Sample movie",
        "description": "Sample description",
        "duration": 90,
    }
    defaults.update(params)

    return Movie.objects.create(**defaults)


def sample_movie_session(**params):
    cinema_hall = CinemaHall.objects.create(
        name="Blue", rows=20, seats_in_row=20
    )

    defaults = {
        "show_time": "2022-06-02 14:00:00",
        "movie": None,
        "cinema_hall": cinema_hall,
    }
    defaults.update(params)

    return MovieSession.objects.create(**defaults)


def image_upload_url(movie_id):
    """Return URL for recipe image upload"""
    return reverse("cinema:movie-upload-image", args=[movie_id])


def detail_url(movie_id):
    return reverse("cinema:movie-detail", args=[movie_id])


class UnauthenticatedMovieApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_auth_required(self):
        res = self.client.get(MOVIE_URL)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class AuthenticatedMovieApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            "test@test.com",
            "testpass",
        )
        self.client.force_authenticate(self.user)

    def test_list_movies(self):
        sample_movie()
        sample_movie()

        res = self.client.get(MOVIE_URL)

        movies = Movie.objects.all().order_by("id")
        serializer = MovieListSerializer(movies, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_filter_movies_by_genres(self):
        genre1 = Genre.objects.create(name="Genre 1")
        genre2 = Genre.objects.create(name="Genre 2")

        movie1 = sample_movie(title="Movie 1")
        movie2 = sample_movie(title="Movie 2")

        movie1.genres.add(genre1)
        movie2.genres.add(genre2)

        movie3 = sample_movie(title="Movie without genres")

        res = self.client.get(
            MOVIE_URL, {"genres": f"{genre1.id},{genre2.id}"}
        )

        serializer1 = MovieListSerializer(movie1)
        serializer2 = MovieListSerializer(movie2)
        serializer3 = MovieListSerializer(movie3)

        self.assertIn(serializer1.data, res.data)
        self.assertIn(serializer2.data, res.data)
        self.assertNotIn(serializer3.data, res.data)

    def test_filter_movies_by_actors(self):
        actor1 = Actor.objects.create(first_name="Actor 1", last_name="Last 1")
        actor2 = Actor.objects.create(first_name="Actor 2", last_name="Last 2")

        movie1 = sample_movie(title="Movie 1")
        movie2 = sample_movie(title="Movie 2")

        movie1.actors.add(actor1)
        movie2.actors.add(actor2)

        movie3 = sample_movie(title="Movie without actors")

        res = self.client.get(
            MOVIE_URL, {"actors": f"{actor1.id},{actor2.id}"}
        )

        serializer1 = MovieListSerializer(movie1)
        serializer2 = MovieListSerializer(movie2)
        serializer3 = MovieListSerializer(movie3)

        self.assertIn(serializer1.data, res.data)
        self.assertIn(serializer2.data, res.data)
        self.assertNotIn(serializer3.data, res.data)

    def test_filter_movies_by_title(self):
        movie1 = sample_movie(title="Movie")
        movie2 = sample_movie(title="Another Movie")
        movie3 = sample_movie(title="No match")

        res = self.client.get(MOVIE_URL, {"title": "movie"})

        serializer1 = MovieListSerializer(movie1)
        serializer2 = MovieListSerializer(movie2)
        serializer3 = MovieListSerializer(movie3)

        self.assertIn(serializer1.data, res.data)
        self.assertIn(serializer2.data, res.data)
        self.assertNotIn(serializer3.data, res.data)

    def test_retrieve_movie_detail(self):
        movie = sample_movie()
        movie.genres.add(Genre.objects.create(name="Genre"))
        movie.actors.add(
            Actor.objects.create(first_name="Actor", last_name="Last")
        )

        url = detail_url(movie.id)
        res = self.client.get(url)

        serializer = MovieDetailSerializer(movie)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_create_movie_forbidden(self):
        payload = {
            "title": "Movie",
            "description": "Description",
            "duration": 90,
        }
        res = self.client.post(MOVIE_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)


class AdminMovieApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            "admin@admin.com", "testpass", is_staff=True
        )
        self.client.force_authenticate(self.user)

    def test_create_movie(self):
        payload = {
            "title": "Movie",
            "description": "Description",
            "duration": 90,
        }
        res = self.client.post(MOVIE_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        movie = Movie.objects.get(id=res.data["id"])
        for key in payload.keys():
            self.assertEqual(payload[key], getattr(movie, key))

    def test_create_movie_with_genres(self):
        genre1 = Genre.objects.create(name="Action")
        genre2 = Genre.objects.create(name="Adventure")
        payload = {
            "title": "Spider Man",
            "genres": [genre1.id, genre2.id],
            "description": "With Spider-Man's identity now revealed, Peter asks Doctor Strange for help.",
            "duration": 148,
        }
        res = self.client.post(MOVIE_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        movie = Movie.objects.get(id=res.data["id"])
        genres = movie.genres.all()
        self.assertEqual(genres.count(), 2)
        self.assertIn(genre1, genres)
        self.assertIn(genre2, genres)

    def test_create_movie_with_actors(self):
        actor1 = Actor.objects.create(first_name="Tom", last_name="Holland")
        actor2 = Actor.objects.create(first_name="Tobey", last_name="Maguire")
        payload = {
            "title": "Spider Man",
            "actors": [actor1.id, actor2.id],
            "description": "With Spider-Man's identity now revealed, Peter asks Doctor Strange for help.",
            "duration": 148,
        }
        res = self.client.post(MOVIE_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        movie = Movie.objects.get(id=res.data["id"])
        actors = movie.actors.all()
        self.assertEqual(actors.count(), 2)
        self.assertIn(actor1, actors)
        self.assertIn(actor2, actors)


class MovieImageUploadTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_superuser(
            "admin@myproject.com", "password"
        )
        self.client.force_authenticate(self.user)
        self.movie = sample_movie()
        self.movie_session = sample_movie_session(movie=self.movie)

    def tearDown(self):
        self.movie.image.delete()

    def test_upload_image_to_movie(self):
        """Test uploading an image to movie"""
        url = image_upload_url(self.movie.id)
        with tempfile.NamedTemporaryFile(suffix=".jpg") as ntf:
            img = Image.new("RGB", (10, 10))
            img.save(ntf, format="JPEG")
            ntf.seek(0)
            res = self.client.post(url, {"image": ntf}, format="multipart")
        self.movie.refresh_from_db()

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertIn("image", res.data)
        self.assertTrue(os.path.exists(self.movie.image.path))

    def test_upload_image_bad_request(self):
        """Test uploading an invalid image"""
        url = image_upload_url(self.movie.id)
        res = self.client.post(url, {"image": "not image"}, format="multipart")

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_image_to_movie_list_should_not_work(self):
        url = MOVIE_URL
        with tempfile.NamedTemporaryFile(suffix=".jpg") as ntf:
            img = Image.new("RGB", (10, 10))
            img.save(ntf, format="JPEG")
            ntf.seek(0)
            res = self.client.post(
                url,
                {
                    "title": "Title",
                    "description": "Description",
                    "duration": 90,
                    "image": ntf,
                },
                format="multipart",
            )

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        movie = Movie.objects.get(title="Title")
        self.assertFalse(movie.image)

    def test_image_url_is_shown_on_movie_detail(self):
        url = image_upload_url(self.movie.id)
        with tempfile.NamedTemporaryFile(suffix=".jpg") as ntf:
            img = Image.new("RGB", (10, 10))
            img.save(ntf, format="JPEG")
            ntf.seek(0)
            self.client.post(url, {"image": ntf}, format="multipart")
        res = self.client.get(detail_url(self.movie.id))

        self.assertIn("image", res.data)

    def test_image_url_is_shown_on_movie_list(self):
        url = image_upload_url(self.movie.id)
        with tempfile.NamedTemporaryFile(suffix=".jpg") as ntf:
            img = Image.new("RGB", (10, 10))
            img.save(ntf, format="JPEG")
            ntf.seek(0)
            self.client.post(url, {"image": ntf}, format="multipart")
        res = self.client.get(MOVIE_URL)

        self.assertIn("image", res.data[0].keys())

    def test_image_url_is_shown_on_movie_session_detail(self):
        url = image_upload_url(self.movie.id)
        with tempfile.NamedTemporaryFile(suffix=".jpg") as ntf:
            img = Image.new("RGB", (10, 10))
            img.save(ntf, format="JPEG")
            ntf.seek(0)
            self.client.post(url, {"image": ntf}, format="multipart")
        res = self.client.get(MOVIE_SESSION_URL)

        self.assertIn("movie_image", res.data[0].keys())

    def test_put_movie_not_allowed(self):
        payload = {
            "title": "New movie",
            "description": "New description",
            "duration": 98,
        }

        movie = sample_movie()
        url = detail_url(movie.id)

        res = self.client.put(url, payload)

        self.assertEqual(res.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_delete_movie_not_allowed(self):
        movie = sample_movie()
        url = detail_url(movie.id)

        res = self.client.delete(url)

        self.assertEqual(res.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
