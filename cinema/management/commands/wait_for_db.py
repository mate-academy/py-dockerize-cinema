from django.core.management.base import BaseCommand
import time


class Command(BaseCommand):
    help_ = "Waits for db before starting the server"

    def handle(self, *args, **options):
        time.sleep(2)
        self.stdout.write(
            self.style.SUCCESS("No more sleeping")
        )
