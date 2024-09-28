from django.core.management.base import BaseCommand
import time
import psycopg2
from django.conf import settings
from psycopg import OperationalError


class Command(BaseCommand):
    help = "Wait for the database to be available." # noqa

    def handle(self, *args, **kwargs):
        db_config = settings.DATABASES["default"]

        while True:
            try:
                conn = psycopg2.connect(
                    dbname=db_config["NAME"],
                    user=db_config["USER"],
                    password=db_config["PASSWORD"],
                    host=db_config["HOST"],
                    port=db_config["PORT"],
                )
                conn.close()
                self.stdout.write(self.style.SUCCESS("Database available!"))
                break
            except OperationalError as e:
                self.stdout.write(e)
                time.sleep(1)
