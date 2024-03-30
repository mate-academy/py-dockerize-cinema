from time import sleep

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    helps = "Make program sleep for n seconds"

    def add_arguments(self, parser):
        parser.add_argument("seconds", type=int)

    def handle(self, *args, **options):
        seconds = options.get("seconds")
        sleep(seconds)
        print(f"Waiting {seconds} seconds ...")
