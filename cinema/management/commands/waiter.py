from django.core.management.base import BaseCommand
from time import sleep


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")
        sleep(1)
