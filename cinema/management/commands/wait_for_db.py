import time
from django.core.management.base import BaseCommand, CommandError
from django.db import connection
from django.db.utils import OperationalError


class Command(BaseCommand):

    def handle(self, *args, **options):

        for _ in range(10):

            try:
                with connection.cursor():
                    print("DB is available!")
                    return
            except OperationalError:
                print("DB is unavailable, waiting 1 second...")
                time.sleep(1)
        raise CommandError("DB is unavailable after 10 attempts.")
