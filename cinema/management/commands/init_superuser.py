import os

from django.contrib.auth import get_user_model
from django.core.management import BaseCommand
from django.db import IntegrityError


class Command(BaseCommand):
    """Django command to init superuser while no any user in db"""

    def handle(self, *args, **options):
        self.email = os.environ.get("SUPER_USER")
        self.password = os.environ.get("SUPER_PASSWORD")
        if (
                get_user_model().objects.count() == 0
                and self.email
                and self.password
        ):
            self.stdout.write("Init superuser for database...")
            try:
                self.admin = get_user_model().objects.create_superuser(
                    email=self.email,
                    password=self.password
                )
            except (ValueError, IntegrityError):
                self.stdout.write("Error: Not created...")
            else:
                self.stdout.write(f"Created superuser {self.email}")
        else:
            self.stdout.write(
                "Superuser can be initialized with no blank email & password "
                "only if no any user yet"
            )
