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

        movies = Movie.objects.order_by("id")
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


def create_actor(first_name, last_name):
    """Helper function to create an actor"""
    return Actor.objects.create(first_name=first_name, last_name=last_name)


def create_genre(name):
    """Helper function to create a genre"""
    return Genre.objects.create(name=name)


def create_movie(**params):
    """Helper function to create a movie"""
    defaults = {
        "title": "Test Movie",
        "description": "A description of the test movie",
        "duration": 120,
    }
    defaults.update(params)
    movie = Movie.objects.create(**defaults)
    return movie


class PublicMovieApiTests(TestCase):
    """Test unauthenticated movie API access"""

    def setUp(self):
        self.client = APIClient()

    def test_auth_required(self):
        """Test that authentication is required"""
        res = self.client.get(MOVIE_URL)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateMovieApiTests(TestCase):
    """Test authenticated movie API access"""

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            "test@example.com", "password123"
        )
        self.client.force_authenticate(self.user)

        # Create test actors and genres
        self.actor1 = create_actor("John", "Doe")
        self.actor2 = create_actor("Jane", "Smith")
        self.genre1 = create_genre("Action")
        self.genre2 = create_genre("Drama")

    def test_retrieve_movies(self):
        """Test retrieving a list of movies"""
        create_movie()
        create_movie(title="Another Movie", duration=150)

        res = self.client.get(MOVIE_URL)

        movies = Movie.objects.all().order_by("title")
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), len(movies))

    def test_create_movie(self):
        """Test creating a movie"""
        payload = {
            "title": "New Movie",
            "description": "Some description",
            "duration": 150,
            "genres": [self.genre1.id, self.genre2.id],
            "actors": [self.actor1.id, self.actor2.id],
        }
        res = self.client.post(MOVIE_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        movie = Movie.objects.get(id=res.data["id"])
        self.assertEqual(movie.title, payload["title"])
        self.assertEqual(movie.description, payload["description"])
        self.assertEqual(movie.duration, payload["duration"])
        self.assertEqual(movie.genres.count(), 2)
        self.assertEqual(movie.actors.count(), 2)

    def test_create_movie_with_invalid_data(self):
        """Test creating a movie with invalid data fails"""
        payload = {"title": "", "duration": -10}
        res = self.client.post(MOVIE_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_filter_movies_by_genres(self):
        """Test filtering movies by genres"""
        movie1 = create_movie(title="Movie 1")
        movie2 = create_movie(title="Movie 2")

        movie1.genres.add(self.genre1)
        movie2.genres.add(self.genre2)

        res = self.client.get(MOVIE_URL, {"genres": f"{self.genre1.id}"})

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)
        self.assertEqual(res.data[0]["title"], movie1.title)

    def test_filter_movies_by_actors(self):
        """Test filtering movies by actors"""
        movie1 = create_movie(title="Movie 1")
        movie2 = create_movie(title="Movie 2")

        movie1.actors.add(self.actor1)
        movie2.actors.add(self.actor2)

        res = self.client.get(MOVIE_URL, {"actors": f"{self.actor1.id}"})

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)
        self.assertEqual(res.data[0]["title"], movie1.title)

    def test_upload_image(self):
        """Test uploading an image to a movie"""
        movie = create_movie()
        url = reverse("cinema:movie-upload-image", args=[movie.id])

        with open("path/to/your/test-image.jpg", "rb") as image:
            res = self.client.post(url, {"image": image}, format="multipart")

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        movie.refresh_from_db()
        self.assertIn("test-image", movie.image.url)

    def test_post_image_to_movie_list_should_not_work(self):
        """Test that posting an image to movie list endpoint should not work"""
        with open("path/to/your/test-image.jpg", "rb") as image:
            res = self.client.post(MOVIE_URL, {"image": image}, format="multipart")

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
