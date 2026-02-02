from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    MovieViewSet, ActorViewSet, GenreViewSet, OrderViewSet, MovieSessionViewSet, CinemaHallViewSet,
)

app_name = "cinema"

router = routers.DefaultRouter()
router.register("movies", MovieViewSet, basename="movies")
router.register("actors", ActorViewSet, basename="actors")
router.register("genres", GenreViewSet, basename="genres")
router.register("orders", OrderViewSet, basename="orders")
router.register("cinemahall", CinemaHallViewSet, basename="cinemahall")
router.register("movie_sessions", MovieSessionViewSet, basename="movie_sessions")

urlpatterns = [path("", include(router.urls)),
]