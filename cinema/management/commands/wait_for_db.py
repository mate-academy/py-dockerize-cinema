import os
from time import sleep

import psycopg2
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Wait for db" # noqa

    def handle(self, *args, **options):
        while True:
            try:
                psycopg2.connect(
                    f"dbname={os.environ['POSTGRES_DB']} "
                    f"user={os.environ['POSTGRES_USER']} "
                    f"host={os.environ['POSTGRES_HOST']} "
                    f"password={os.environ['POSTGRES_PASSWORD']}")
                break
            except psycopg2.Error:
                print("Trying to connect failed")
                sleep(0.1)
