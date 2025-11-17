import time

from django.db import connection
from django.core.management.base import BaseCommand
from psycopg import OperationalError


class Command(BaseCommand):
    def handle(self, *args, **options):
        limit = 15
        num = 0
        while num != limit:
            try:
                connection.ensure_connection()
                print("Connection established")
                break
            except OperationalError as e:
                print("Database is not ready", e)
                num += 1
                time.sleep(1)
        if num == limit:
            raise ConnectionError("Cannot connect to database")
