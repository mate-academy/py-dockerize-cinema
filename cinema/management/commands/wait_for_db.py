import time
from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):
    help_message = "Waiting for db."

    def handle(self, *args, **kwargs):
        self.stdout.write("⏳ Waiting for db...")
        db_conn = None
        retries = 10

        while not db_conn and retries > 0:
            try:
                db_conn = connections["default"]
                db_conn.cursor()
            except OperationalError:
                retries -= 1
                self.stdout.write("🚧 DB is not available. Retry in 3 sec...")
                time.sleep(3)

        if not db_conn:
            self.stderr.write("❌ Failed to connect to db!")
            self.exit(1)

        self.stdout.write(self.style.SUCCESS("✅ DB is available!"))
