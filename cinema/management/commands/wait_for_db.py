import os
from time import sleep

import psycopg2

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Checks the connection to database"

    def handle(self, *args, **options):
        try:
            psycopg2.connect(
                f"dbname={os.environ['POSTGRES_DB']} "
                f"user={os.environ['POSTGRES_USER']} "
                f"password={os.environ['POSTGRES_PASSWORD']} "
                f"host={os.environ['POSTGRES_HOST']}"
            )
        except psycopg2.OperationalError:
            sleep(5)
            self.handle(*args, **options)
        else:
            self.stdout.write(
                self.style.SUCCESS("Connection to database established")
            )
