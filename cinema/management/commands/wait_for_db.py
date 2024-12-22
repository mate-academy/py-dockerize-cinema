from time import sleep

import backoff
from django.core.management import BaseCommand
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):

    @backoff.on_exception(
        backoff.expo,
        OperationalError,
        max_time=60
    )
    def connect(self):
        connections["default"].ensure_connection()
        self.stdout.write(self.style.SUCCESS("Connected successfully!"))

    def handle(self, *args, **kwargs):
        self.stdout.write("Connecting to database...")
        self.connect()
