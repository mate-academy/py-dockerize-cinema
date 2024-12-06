import os
import time

from django.core.management.base import (
    BaseCommand,
    CommandParser,
    DjangoHelpFormatter
)
from django.db import OperationalError
from django.db import connection

WAITING = 1


class Command(BaseCommand):
    help_prevent_shadow_builtins = "Waits for the database to be available"

    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")
        db_conn = None
        while not db_conn:
            try:
                connection.ensure_connection()
                db_conn = True
            except OperationalError:
                self.stdout.write(f"Database unavailable, waiting"
                                  f" {WAITING} second...")
                time.sleep(WAITING)

    def create_parser(self, prog_name, subcommand, **kwargs):
        """
        Create and return the ``ArgumentParser`` which will be used to
        parse the arguments to this command.
        """
        parser = CommandParser(
            prog="%s %s" % (os.path.basename(prog_name), subcommand),
            description=self.help_prevent_shadow_builtins or None,
            formatter_class=DjangoHelpFormatter,
            missing_args_message=getattr(self, "missing_args_message", None),
            called_from_command_line=getattr(
                self,
                "_called_from_command_line",
                None
            ),
            **kwargs,
        )
        return parser
