from datetime import time

from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write("Waiting for database")
        db = None
        try:
            while db is None:
                try:
                    db = self.check(databases=["default"])
                except Exception:
                    self.stdout.write(
                        "Database unavailable, waiting 1 second..."
                    )
                    time.sleep(1)
            self.stdout.write(self.style.SUCCESS("Database available!"))
        except Exception as e:
            raise CommandError(str(e))
