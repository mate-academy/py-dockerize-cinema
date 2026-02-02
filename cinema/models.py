import uuid

from pathlib import Path
from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.text import slugify


class Genre(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Actor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class CinemaHall(models.Model):
    name = models.CharField(max_length=100)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()

    @property
    def capacity(self):
        return self.rows * self.seats_in_row

    def __str__(self):
        return f"CinemaHall: {self.name} (rows: {self.rows}, seats_in_row: {self.seats_in_row})"

def movie_upload_path(instance: "Movie", filename: str) -> Path:
    filename = f"{slugify(instance.title)}-{uuid.uuid4()}" + Path(filename).suffix
    return Path("upload/movies/") / Path(filename)


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    genres = models.ManyToManyField(
        Genre,
        related_name="movies",
    )
    actors = models.ManyToManyField(
        Actor,
        related_name="movies",
        blank=True,
    )
    duration = models.IntegerField()

    image = models.ImageField(
        null=True,
        upload_to=movie_upload_path
    )

    class Meta:
        verbose_name_plural = "movies"

    def __str__(self):
        return f"Movie: {self.title} - {self.duration} ({self.description})"

class MovieSession(models.Model):
    show_time = models.DateTimeField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    cinema_hall = models.ForeignKey(CinemaHall, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-show_time"]

    def __str__(self):
        return self.movie.title + " " + str(self.show_time)


class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="orders",
    )

    def __str__(self):
        return str(self.created_at)

    class Meta:
        ordering = ["-created_at"]


class Ticket(models.Model):
    movie_session = models.ForeignKey(
        MovieSession,
        on_delete=models.CASCADE,
        related_name="tickets",
    )
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="tickets",
    )
    row = models.IntegerField()
    seat = models.IntegerField()

    def clean(self):
        for ticket_attr_value, ticket_attr_name, cinema_hall_attr_name in [
            (self.row, "row", "rows"),
            (self.seat, "seat", "seats_in_row"),
        ]:
            count_attrs = getattr(
                self.movie_session.cinema_hall, cinema_hall_attr_name
            )
            if not (1 <= ticket_attr_value <= count_attrs):
                raise ValidationError(
                    {
                        ticket_attr_name: f"{ticket_attr_name} number "
                                          f"must be in available range: "
                                          f"(1, {cinema_hall_attr_name}): "
                                          f"(1, {count_attrs})"
                    }
                )

    def __str__(self):
        return (
            f"{str(self.movie_session)} (row: {self.row}, seat: {self.seat})"
        )

    class Meta:
        unique_together = ("movie_session", "row", "seat")
