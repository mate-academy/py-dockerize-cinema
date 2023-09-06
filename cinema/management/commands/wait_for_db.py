import time

import psycopg2
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    @staticmethod
    def check_database_health(host, port, user, password, database):
        # Connect to the database
        conn = psycopg2.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database
        )
        cursor = conn.cursor()

        # Run a simple query to check the health of the database
        cursor.execute("SELECT 1")
        result = cursor.fetchone()

        # Check the result of the query
        if result == (1,):
            return 1
        return 0

    def handle(self, *args, **options):
        try:
            Command.check_database_health(
                host="db",
                port=5432,
                user="postgres",
                password="12361236",
                database="postgres")
        except psycopg2.OperationalError:
            time.sleep(3)
            Command.handle(self, *args, **options)
