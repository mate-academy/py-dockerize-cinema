import psycopg2
from django.core.management.base import BaseCommand, CommandError
from psycopg2 import OperationalError


class Command(BaseCommand):

    def handle(self, *args, **options):
        try:
            psycopg2.connect(**options)
        except OperationalError as e:
            self.stdout.write(f"The error '{e}' occurred")

        self.stdout.write(
            self.style.SUCCESS("Successfully connected to database")
        )
