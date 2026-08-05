from time import sleep

from django.core.management import BaseCommand
from django.db import connections
from psycopg import OperationalError


class Command(BaseCommand):

    def handle(self, *args, **options):
        db_up = False
        while not db_up:
            try:
                db_con = connections["default"]
                db_con.cursor()
                db_up = True
            except OperationalError:
                sleep(3)
