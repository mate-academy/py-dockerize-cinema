import sys
import time

from django.core.management.base import BaseCommand
from django.db import connection
from django.db.utils import OperationalError


class Command(BaseCommand):
    help = "Wait for db"

    def add_arguments(self, parser):
        parser.add_argument("--max_retries", type=int, default=60)

    def handle(self, *args, **options):
        max_retries = options["max_retries"]

        for retry in range(max_retries):
            try:
                connection.ensure_connection()
                self.stdout.write(self.style.SUCCESS("Connection Success"))
            except OperationalError as e:
                self.stdout.write(
                    f"Database unavailable on attempt "
                    f"{retry+1}/{max_retries}: {e}"
                )
                time.sleep(3)
            else:
                break
        else:
            self.stdout.write(self.style.ERROR("Database unavailable"))
            sys.exit(1)
