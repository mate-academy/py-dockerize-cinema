import time

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Waiting for database will be available"

    def handle(self, *args, **options):
        time.sleep(5)
