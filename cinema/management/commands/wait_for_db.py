import time
from django.core.management.base import BaseCommand
from django.db import connection
from django.db.utils import OperationalError



class Command(BaseCommand):
    help = "Wait for the database"

    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")
        db_conn = None
        while not db_conn:
            try:
                with  connection.cursor() as cursor:
                    cursor.execute("SELECT 1")
                db_conn = True
            except OperationalError:
                self.stdout.write("Database connection failed.")
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS("Database connection successful."))