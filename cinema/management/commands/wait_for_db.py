import os
import time

import psycopg2
from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):
    def handle(self, *args, **options):
        """Wait for PostgreSQL to become available."""

        self.stdout.write("Waiting for PostgreSQL...")

        db_conn = None
        while not db_conn:
            try:
                db_conn = psycopg2.connect(
                    dbname=os.environ.get("POSTGRES_DB"),
                    user=os.environ.get("POSTGRES_USER"),
                    password=os.environ.get("POSTGRES_PASSWORD"),
                    host=os.environ.get("POSTGRES_HOST"),
                    port=os.environ.get("POSTGRES_PORT"),
                )
            except psycopg2.OperationalError:
                self.stdout.write("PostgreSQL is unavailable - sleeping")
                time.sleep(1)

        db_conn.close()
        self.stdout.write(
            self.style.SUCCESS("PostgreSQL is up - " "connecting to Django")
        )

        db_conn = None
        while not db_conn:
            try:
                connections["default"].connect()
                db_conn = True
            except OperationalError:
                self.stdout.write("Django is unavailable - sleeping")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Django is up - ready to go!"))
