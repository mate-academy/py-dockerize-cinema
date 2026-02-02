import datetime

from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

from cinema.models import MovieSession, Movie, CinemaHall
from cinema.tests.test_movie_api import sample_actor
from cinema.tests.test_cinema_hall_api import sample_cinema_hall
from cinema.tests.test_genre_api import sample_genres
from cinema.tests.test_movie_api import sample_movie
from user.tests.test_user_api import create_user
from cinema.serializers import MovieSessionRetrieveSerializer

MOVIE_SESSION_URL = reverse("cinema:movie_sessions-list")


def sample_movie_session(**params):
    genres = sample_genres()
    actors = sample_actor()
    movie = sample_movie()

    movie.genres.add(genres)
    movie.actors.add(actors)

    cinema_hall = sample_cinema_hall()

    defaults = {
        "movie": movie,
        "cinema_hall": cinema_hall,
        "show_time": datetime.datetime(
            year=2022,
            month=9,
            day=2,
        ),
    }
    defaults.update(params)

    return MovieSession.objects.create(**defaults)


def detail_url(movie_session_id):
    return reverse("cinema:movie_sessions-detail", args=[movie_session_id])


class PublicMovieSessionApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_auth_required(self):
        res = self.client.get(MOVIE_SESSION_URL)
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)


class PrivateMovieSessionApiTests(TestCase):
    def setUp(self):
        self.user = create_user(
            email="test@test.com",
            password="testpass",
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_get_movie_sessions(self):
        sample_movie_session()

        movie_sessions = self.client.get(MOVIE_SESSION_URL)
        self.assertEqual(movie_sessions.status_code, status.HTTP_200_OK)

    def test_retrieve_movie_session(self):
        movie_session = sample_movie_session()

        url = detail_url(movie_session.id)
        response = self.client.get(url)

        serializer = MovieSessionRetrieveSerializer(movie_session, many=False)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_post_movie_session(self):
        response = self.client.post(MOVIE_SESSION_URL, {})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_put_movie_session(self):
        movie_session = sample_movie_session()

        url = detail_url(movie_session.id)
        response = self.client.put(url, {})

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_movie_session(self):
        movie_session = sample_movie_session()

        url = detail_url(movie_session.id)
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class AdminMovieSessionApiTests(TestCase):
    def setUp(self):
        self.user = create_user(
            email="test@test.com",
            password="testpass",
            is_staff=True,
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_post_movie_session(self):
        payload = {}

        response = self.client.post(MOVIE_SESSION_URL, payload)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_put_movie_session(self):
        movie_session = sample_movie_session()

        url = detail_url(movie_session.id)
        payload = {}

        response = self.client.put(url, payload)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_movie_session(self):
        movie_session = sample_movie_session()

        url = detail_url(movie_session.id)
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
