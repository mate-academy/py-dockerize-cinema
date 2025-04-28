import os
import time
import psycopg2
from psycopg2 import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        self.stdout.write("Waiting for database...")
        db_up = False
        while db_up is False:
            try:
                psycopg2.connect(
                    dbname=os.environ.get("POSTGRES_DB"),
                    user=os.environ.get("POSTGRES_USER"),
                    password=os.environ.get("POSTGRES_PASSWORD"),
                    host=os.environ.get("DB_HOST"),
                    port=os.environ.get("DB_PORT", "5433"),
                )
                db_up = True
            except OperationalError:
                self.stdout.write("Database unavailable, waiting 1 second...")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database available!"))
