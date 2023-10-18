import time
from django.db import connections
from django.db.utils import OperationalError
from django.core.management import BaseCommand


class Command(BaseCommand):
    help = "Wait for the database to become available"

    def add_arguments(self, parser) -> None:
        """Add command-line arguments for database waiting."""

        parser.add_argument(
            "--max-retries",
            type=int,
            default=30,
            help="Maximum number of retry attempts",
        )
        parser.add_argument(
            "--wait-seconds",
            type=int,
            default=1,
            help="Number of seconds to wait between retry attempts",
        )

    def handle(self, *args, **options) -> None:
        """
           Wait for the database to become available.

           This method attempts to establish a connection
           to the default database and waits for it to become available.
           It will retry a specified number of times
           with a wait time between retries.
        """
        max_retries: int = options["max-retries"]
        wait_seconds: int = options["wait-seconds"]

        self.stdout.write("Waiting for the database ...")

        db_conn = None
        retries = 0
        while not db_conn and retries < max_retries:
            try:
                db_conn = connections["default"].cursor()
            except OperationalError:
                self.stdout.write(
                    "Database unavailable, waiting {} seconds ...".format(wait_seconds)
                )
                time.sleep(wait_seconds)
                retries += 1

        if db_conn:
            self.stdout.write(self.style.SUCCESS("Database is available!"))
        else:
            self.stdout.write(self.style.ERROR("Unable to connect to the database. Max retries reached."))
