from django.core.management.base import BaseCommand
from django.db import connection
import time


class Command(BaseCommand):
    """ Django command to pause execution until database is available"""
    def handle(self, *args, **kwargs):
        self.stdout.write("waiting for db ...")
        db_conn = None
        while not db_conn:
            try:
                with connection.cursor() as cursor:
                    cursor.execute("SELECT 1")
                return "Connected to db"
            except Exception as e:
                print(str(e))
                time.sleep(1)
