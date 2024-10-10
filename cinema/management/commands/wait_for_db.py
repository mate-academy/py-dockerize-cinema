import time
import psycopg2
from django.core.management.base import BaseCommand
from django.conf import settings
from psycopg2 import OperationalError


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        db_settings = settings.DATABASES["default"]

        while True:
            try:
                conn = psycopg2.connect(
                    dbname=db_settings["NAME"],
                    user=db_settings["USER"],
                    password=db_settings["PASSWORD"],
                    host=db_settings["HOST"],
                    port=db_settings["PORT"],
                )
                conn.close()
                self.stdout.write(self.style.SUCCESS("Database available!"))
                break
            except OperationalError as e:
                self.stdout.write(
                    f"Database unavailable, waiting 1 second... ({e})"
                )
                time.sleep(1)
