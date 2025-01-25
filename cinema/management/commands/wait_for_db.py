import os
from time import sleep

import psycopg
from django.core.management.base import BaseCommand, CommandError
from dotenv import load_dotenv


class Command(BaseCommand):
    help = "Waiting for database connection"
    load_dotenv()

    def handle(self, *args, **options):
        count = 0
        max_count = 4
        while count < max_count:
            count += 1
            try:
                conn = psycopg.connect(
                    f"dbname={os.getenv("POSTGRES_DB")} "
                    f"user={os.getenv("POSTGRES_USER")} "
                    f"host={os.getenv("POSTGRES_HOST")} "
                    f"password={os.getenv("POSTGRES_PASSWORD")}"
                )
                conn.close()
                self.stdout.write(
                    self.style.SUCCESS(
                        "Database connection successful!"
                    )
                )
                break
            except psycopg.OperationalError:
                self.stdout.write(
                    self.style.ERROR(
                        "Database unavailable, retrying..."
                    )
                )
                sleep(3)
                if count == max_count:
                    raise CommandError(
                        "Max attempts exceeded. "
                        "Wasn't able to connect. Exiting..."
                    )
