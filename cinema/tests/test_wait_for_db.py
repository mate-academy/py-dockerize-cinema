from io import StringIO
from unittest.mock import MagicMock, patch

from django.core.management import call_command
from django.core.management.base import CommandError
from django.db.utils import InterfaceError, OperationalError
from django.test import SimpleTestCase


class WaitForDatabaseTests(SimpleTestCase):
    def setUp(self):
        self.connection = MagicMock()
        self.connections = patch(
            "cinema.management.commands.wait_for_db.connections",
            {"default": self.connection},
        )
        self.connections.start()
        self.addCleanup(self.connections.stop)
        self.output = StringIO()

    def test_ready_database(self):
        call_command("wait_for_db", stdout=self.output)
        cursor = self.connection.cursor.return_value.__enter__.return_value
        cursor.execute.assert_called_once_with("SELECT 1")
        self.assertIn("Database available!", self.output.getvalue())

    @patch("cinema.management.commands.wait_for_db.time.sleep")
    def test_retries_until_query_succeeds(self, sleep):
        ready_cursor = MagicMock()
        self.connection.cursor.side_effect = [
            OperationalError(), InterfaceError(), ready_cursor,
        ]
        call_command("wait_for_db", stdout=self.output)
        self.assertEqual(self.connection.cursor.call_count, 3)
        self.assertEqual(self.connection.close.call_count, 2)
        self.assertEqual(sleep.call_count, 2)

    @patch("cinema.management.commands.wait_for_db.time.monotonic")
    @patch("cinema.management.commands.wait_for_db.time.sleep")
    def test_timeout(self, sleep, monotonic):
        monotonic.side_effect = [0, 1, 3]
        self.connection.cursor.side_effect = OperationalError()
        with self.assertRaisesMessage(CommandError, "Database unavailable"):
            call_command("wait_for_db", timeout=2, stdout=self.output)
        sleep.assert_called_once_with(1)

    def test_invalid_retry_options(self):
        for options in ({"timeout": 0}, {"interval": -1}):
            with self.subTest(options=options):
                with self.assertRaisesMessage(CommandError, "positive"):
                    call_command("wait_for_db", stdout=self.output, **options)
        self.connection.cursor.assert_not_called()

    def test_non_finite_retry_options_are_rejected(self):
        for name in ("timeout", "interval"):
            for value in (float("nan"), float("inf"), float("-inf")):
                with self.subTest(name=name, value=value):
                    with self.assertRaisesMessage(CommandError, "finite"):
                        call_command(
                            "wait_for_db", stdout=self.output,
                            **{name: value},
                        )
        self.connection.cursor.assert_not_called()

    def test_unexpected_error_is_not_hidden(self):
        self.connection.cursor.side_effect = ValueError("invalid config")
        with self.assertRaisesMessage(ValueError, "invalid config"):
            call_command("wait_for_db", stdout=self.output)
