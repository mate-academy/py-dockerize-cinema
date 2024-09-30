import os

import psycopg2
from django.core.management import BaseCommand

from cinema.management.commands._decorators import reconnect


class Command(BaseCommand):
    @reconnect(max_retries=5)
    def handle(self, *args, **options):
        connection = None
        try:
            connection = psycopg2.connect(
                host=os.environ["POSTGRES_HOST"],
                database=os.environ["POSTGRES_DB"],
                user=os.environ["POSTGRES_USER"],
                password=os.environ["POSTGRES_PASSWORD"]
            )
            self.stdout.write(
                self.style.SUCCESS("Successfully connected to database")
            )
        finally:
            if connection:
                connection.close()
