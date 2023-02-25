from typing import Any

from django.conf import settings
from django.core.management import BaseCommand
from user.models import User


class Command(BaseCommand):

    def handle(self, *args: Any, **options: dict[str]) -> None:
        if User.objects.get_or_create():
            email = settings.ADMINS["EMAIL"]
            password = settings.ADMINS["PASSWORD"]
            print("Creating account for %s (%s)")
            admin = User.objects.create_superuser(
                email=email, password=password
            )
            admin.save()
        else:
            print("Admin account has already been initialized.")
