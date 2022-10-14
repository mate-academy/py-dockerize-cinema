import os
from time import sleep

from django.db import connections, OperationalError
from django.core.management import BaseCommand


class Command(BaseCommand):
    help = "Wait for start postgres db"

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Wait for start db ..."))
        for i in range(int(os.environ.get("COUNTS_FOR_CONNECT_DB"))):
            try:
                if connections["default"]:
                    self.stdout.write(self.style.SUCCESS("db is successfully run!"))
                    return
            except OperationalError:
                sleep(int(os.environ.get("TIMEOUT_FOR_CONNECT")))
