import time

from django.core.management.base import BaseCommand, CommandError
from django.db.utils import OperationalError
from django.db import connections


class Command(BaseCommand):
    help = "Waits for the database to be available"

    def add_arguments(self, parser):
        parser.add_argument(
            '--db',
            type=str,
            default='default',
            help='The name of the database connection to wait for'
        )

    def handle(self,  *args, **options):
        db_conn_name = options['db']
        self.stdout.write(f'Waiting for database connection "{db_conn_name}"...')
        db_conn = None

        while not db_conn:
            try:
                db_conn = connections[db_conn_name]
                db_conn.cursor()
            except OperationalError:
                self.stdout.write(f'Database connection "{db_conn_name}" unavailable, waiting 1 second...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS(f'Database connection "{db_conn_name}" available!'))
