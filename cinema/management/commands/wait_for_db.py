from django.core.management.base import BaseCommand
from django.db import connections, OperationalError
from time import sleep


class Command(BaseCommand):

    def handle(self, *args, **options):
        connection = connections["default"]
        for _ in range(10):
            try:
                connection.ensure_connection()
                self.stdout.write(
                    self.style.SUCCESS("Database connection established")
                )
                break
            except OperationalError:
                self.stdout.write(
                    self.style.WARNING("Waiting for db connection 1 sec")
                )
                sleep(1)
        else:
            raise OperationalError(
                "Could not connect to database after 10 attempts"
            )
