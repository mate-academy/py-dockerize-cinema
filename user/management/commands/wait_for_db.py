import time

from django.core.management.base import BaseCommand
from django.db import connection


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")

        while True:
            try:
                connection.ensure_connection()
                break
            except Exception:
                self.stdout.write("Database unavailable, waiting...")
                time.sleep(1)

        self.stdout.write(
            self.style.SUCCESS("Database available!")
        )
