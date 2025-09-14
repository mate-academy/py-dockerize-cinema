import os
import time
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):
    help = "Wait for database to be available"

    def add_arguments(self, parser):
        parser.add_argument(
            "--timeout",
            type=float,
            default=float(os.getenv("WAIT_FOR_DB_TIMEOUT", "60")),
            help="Maximum seconds to wait for DB (default: env WAIT_FOR_DB_TIMEOUT or 60)",
        )
        parser.add_argument(
            "--interval",
            type=float,
            default=float(os.getenv("WAIT_FOR_DB_INTERVAL", "1.0")),
            help="Initial retry interval in seconds (default: env WAIT_FOR_DB_INTERVAL or 1.0)",
        )
        parser.add_argument(
            "--max-interval",
            type=float,
            dest="max_interval",
            default=float(os.getenv("WAIT_FOR_DB_MAX_INTERVAL", "5.0")),
            help="Max backoff interval in seconds (default: env WAIT_FOR_DB_MAX_INTERVAL or 5.0)",
        )

    def handle(self, *args, **options):
        db_cfg = settings.DATABASES.get("default", {})
        host = db_cfg.get("HOST", "localhost")
        port = db_cfg.get("PORT", "5432")
        name = db_cfg.get("NAME", "<unknown>")
        user = db_cfg.get("USER", "<unknown>")

        timeout = options["timeout"]
        interval = options["interval"]
        max_interval = options["max_interval"]

        self.stdout.write(
            f"Waiting for database '{name}' at {host}:{port} as user '{user}'..."
        )

        start = time.monotonic()
        attempt = 0
        delay = max(0.05, float(interval))

        while True:
            try:
                connections["default"].ensure_connection()
                elapsed = time.monotonic() - start
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Database available after {attempt} attempt(s), {elapsed:.2f}s."
                    )
                )
                return
            except OperationalError as exc:
                attempt += 1
                elapsed = time.monotonic() - start
                if elapsed >= timeout:
                    raise CommandError(
                        f"Timed out after {elapsed:.2f}s waiting for DB at {host}:{port} "
                        f"(attempts: {attempt}). Last error: {exc}"
                    )
                self.stdout.write(
                    f"DB not ready (attempt {attempt}, elapsed {elapsed:.2f}s). "
                    f"Retrying in {delay:.2f}s..."
                )
                time.sleep(delay)
                delay = min(delay * 1.5, max_interval)
