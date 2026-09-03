import time

from django.core.management import BaseCommand
from django.db import connection, OperationalError
from psycopg2 import OperationalError as Psycopg2Error


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("waiting for db connection...")
        while True:
            try:
                connection.ensure_connection()
                self.stdout.write("db connection has been established")
                return
            except (OperationalError, Psycopg2Error):
                self.stdout.write("waiting for db connection...")
                time.sleep(1)
