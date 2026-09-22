from io import StringIO
from unittest.mock import call, patch

from django.core.management import call_command
from django.db import OperationalError
from django.test import SimpleTestCase


class WaitForDbTests(SimpleTestCase):
    @patch("cinema.management.commands.wait_for_db.time.sleep")
    @patch(
        "cinema.management.commands.wait_for_db.connection.ensure_connection"
    )
    def test_database_available_immediately(self, ensure_connection, sleep):
        output = StringIO()

        call_command("wait_for_db", stdout=output)

        ensure_connection.assert_called_once_with()
        sleep.assert_not_called()
        self.assertIn("Waiting for database...", output.getvalue())
        self.assertIn("Database available!", output.getvalue())

    @patch("cinema.management.commands.wait_for_db.time.sleep")
    @patch(
        "cinema.management.commands.wait_for_db.connection.ensure_connection"
    )
    def test_retries_until_database_available(self, ensure_connection, sleep):
        ensure_connection.side_effect = [
            OperationalError("Database unavailable"),
            OperationalError("Database unavailable"),
            None,
        ]
        output = StringIO()

        call_command("wait_for_db", stdout=output)

        self.assertEqual(ensure_connection.call_args_list, [call()] * 3)
        self.assertEqual(sleep.call_args_list, [call(1)] * 2)
        self.assertIn("Waiting for database...", output.getvalue())
        self.assertEqual(output.getvalue().count("Database available!"), 1)
