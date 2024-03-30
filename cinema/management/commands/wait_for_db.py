from time import sleep

from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Make program sleep for n seconds"

    def add_arguments(self, parser):
        parser.add_argument("seconds", type=int)

    def handle(self, *args, **options):
        seconds = options.get("seconds")
        sleep(seconds)
        print(f"Waiting {seconds} seconds ...")
