import time
from django.core.management.base import BaseCommand
from django.db import connections, OperationalError


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections["default"]
                with db_conn.cursor() as cursor:
                    cursor.execute("SELECT 1;")
                self.stdout.write(self.style.SUCCESS("Database is available"))
                break
            except OperationalError:
                self.stdout.write("Database is not available, waiting 1 second...")
                time.sleep(1)
