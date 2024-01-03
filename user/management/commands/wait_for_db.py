import os
import time
from psycopg2 import connect, OperationalError
from django.core.management.base import BaseCommand
from django.conf import settings


class Command(BaseCommand):

    def handle(self, *args, **options) -> None:

        for _ in range(10):
            try:
                connect(
                    dbname=settings.DATABASES["default"]["NAME"],
                    host=settings.DATABASES["default"]["HOST"],
                    user=settings.DATABASES["default"]["USER"],
                    password=settings.DATABASES["default"]["PASSWORD"]
                )
                self.stdout.write("Connected to database "
                                  f"{settings.DATABASES['default']['NAME']}")
                break
            except OperationalError:
                self.stdout.write("Wait for database connection...")
                time.sleep(3)
        else:
            self.stdout.write(
                self.style.ERROR("Failed to connect to the database")
            )
