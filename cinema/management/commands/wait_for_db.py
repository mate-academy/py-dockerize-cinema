from django.core.management.base import BaseCommand, no_translations
import time
from django.db import connections


class Command(BaseCommand):
    @no_translations
    def handle(self, *args, **options):
        connection = connections["default"]
        max_attempts = 10
        attempts = 0
        while attempts < max_attempts:
            try:
                connection.ensure_connection()
                self.stdout.write(self.style.SUCCESS("Database is available"))
                break
            except Exception as e:
                attempts += 1
                self.stdout.write(f"Attempt {attempts} failed: {str(e)}")
                time.sleep(1)

        if attempts >= max_attempts:
            self.stdout.write(
                self.style.ERROR("Database is not available. Exiting.")
            )
