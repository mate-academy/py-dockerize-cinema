from __future__ import annotations

import os
import uuid
from typing import Type, Optional, Any

from django.core.exceptions import ValidationError
from django.db import models
from django.conf import settings
from django.utils.text import slugify


class CinemaHall(models.Model):
    name = models.CharField(max_length=255)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()

    @property
    def capacity(self) -> int:
        return self.rows * self.seats_in_row

    def __str__(self) -> str:
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.name


class Actor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.full_name

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"


def movie_image_file_path(instance: Movie, filename: str) -> str:
    _, extension = os.path.splitext(filename)
    filename = f"{slugify(instance.title)}-{uuid.uuid4()}{extension}"

    return os.path.join("uploads/movies/", filename)


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField()
    genres = models.ManyToManyField(Genre, blank=True, related_name="movies")
    actors = models.ManyToManyField(Actor, blank=True, related_name="movies")
    image = models.ImageField(null=True, upload_to=movie_image_file_path)

    class Meta:
        ordering = ["title"]

    def __str__(self) -> str:
        return self.title


class MovieSession(models.Model):
    show_time = models.DateTimeField()
    movie = models.ForeignKey(
        Movie, on_delete=models.CASCADE, related_name="movie_sessions"
    )
    cinema_hall = models.ForeignKey(
        CinemaHall, on_delete=models.CASCADE, related_name="movie_sessions"
    )

    class Meta:
        ordering = ["-show_time"]

    def __str__(self) -> str:
        return self.movie.title + " " + str(self.show_time)


class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="orders",
    )

    def __str__(self) -> str:
        return str(self.created_at)

    class Meta:
        ordering = ["-created_at"]


class Ticket(models.Model):
    movie_session = models.ForeignKey(
        MovieSession, on_delete=models.CASCADE, related_name="tickets"
    )
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="tickets"
    )
    row = models.IntegerField()
    seat = models.IntegerField()

    @staticmethod
    def validate_ticket(
        row: int,
        seat: int,
        cinema_hall: CinemaHall,
        error_to_raise: Type[ValidationError],
    ) -> None:
        for ticket_attr_value, ticket_attr_name, cinema_hall_attr_name in [
            (row, "row", "rows"),
            (seat, "seat", "seats_in_row"),
        ]:
            count_attrs = getattr(cinema_hall, cinema_hall_attr_name)
            if not (1 <= ticket_attr_value <= count_attrs):
                raise error_to_raise(
                    {
                        ticket_attr_name: f"{ticket_attr_name} "
                        f"number must be in available range: "
                        f"(1, {cinema_hall_attr_name}): "
                        f"(1, {count_attrs})"
                    }
                )

    def clean(self) -> None:
        Ticket.validate_ticket(
            self.row,
            self.seat,
            self.movie_session.cinema_hall,
            ValidationError,
        )

    def save(
        self,
        force_insert: bool = False,
        force_update: bool = False,
        using: Optional[Any] = None,
        update_fields: Optional[Any] = None,
    ) -> None:
        self.full_clean()
        return super(Ticket, self).save(
            force_insert, force_update, using, update_fields
        )

    def __str__(self) -> str:
        return (
            f"{str(self.movie_session)} (row: {self.row}, seat: {self.seat})"
        )

    class Meta:
        unique_together = ("movie_session", "row", "seat")
        ordering = ["row", "seat"]
