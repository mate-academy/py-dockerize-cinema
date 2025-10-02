import os
import time
from django.core.management.base import BaseCommand, CommandError
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):
    help = "Aguarda o banco de dados ficar disponível."  # noqa: VNE003

    def handle(self, *args, **options):
        self.stdout.write("Esperando o banco de dados ficar disponível...")

        max_attempts = int(os.environ.get("DB_WAIT_MAX_ATTEMPTS", "30"))
        sleep_sec = float(os.environ.get("DB_WAIT_INITIAL_SLEEP", "1.0"))
        sleep_cap = float(os.environ.get("DB_WAIT_MAX_SLEEP", "5.0"))

        attempt = 0
        while attempt < max_attempts:
            try:
                connections["default"].cursor()
                self.stdout.write(self.style.SUCCESS("Banco de dados disponível!"))
                return
            except OperationalError:
                attempt += 1
                self.stdout.write(
                    f"DB indisponível, tentativa {attempt}/{max_attempts}..."
                )
                time.sleep(sleep_sec)
                sleep_sec = min(sleep_sec * 2, sleep_cap)

        raise CommandError(
            "Banco de dados indisponível após "
            f"{max_attempts} tentativas. Abortando."
        )
