from django.core.management.base import BaseCommand
import time


class Command(BaseCommand):
    def handle(self, *args, **options):
        time.sleep(1)
