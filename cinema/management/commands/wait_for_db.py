from time import sleep

from django.core.management.base import BaseCommand, CommandError

from cinema.models import Genre


class Command(BaseCommand):

    def handle(self, *args, **options):
        for _ in range(5):
            try:
                Genre.objects.all()
                self.stdout.write(
                    self.style.SUCCESS("DB runs successfully")
                )
                return
            except Genre.DoesNotExist:
                sleep(1)

        raise CommandError("DB doesn't exist")
