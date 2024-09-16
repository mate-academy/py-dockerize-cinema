import time

from django.core.management import BaseCommand
from django.db import connection, OperationalError


class Command(BaseCommand):
    help = "Wait until the DB has been raised"  # noqa

    def handle(self, *args, **options):
        self.stdout.write("Wait for the DB starting")
        db_raised = False
        while not db_raised:
            try:
                with connection.cursor() as cursor:
                    cursor.execute("SELECT 1")
            except OperationalError:
                self.stdout.write(
                    "DB connection isn't available. Wait 1 sec..."
                )
                time.sleep(1)
            else:
                db_raised = True
        self.stdout.write(self.style.SUCCESS("DB connection is available!"))
