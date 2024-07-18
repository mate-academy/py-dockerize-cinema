from time import sleep

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Wait 2 seconds for database container is up"

    def handle(self, **kwargs):
        sleep(2)
