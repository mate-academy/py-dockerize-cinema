from io import StringIO
from unittest.mock import call, patch

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase


class WaitForDbTests(SimpleTestCase):
    @patch("time.sleep")
    @patch(
        "django.db.backends.base.base.BaseDatabaseWrapper.ensure_connection"
    )
    def test_returns_immediately_when_database_is_available(
        self, ensure_connection, sleep
    ):
        call_command("wait_for_db", stdout=StringIO())

        ensure_connection.assert_called_once_with()
        sleep.assert_not_called()

    @patch("time.sleep")
    @patch(
        "django.db.backends.base.base.BaseDatabaseWrapper.ensure_connection"
    )
    def test_retries_until_database_is_available(
        self, ensure_connection, sleep
    ):
        ensure_connection.side_effect = [
            OperationalError("Database is starting"),
            OperationalError("Database is starting"),
            None,
        ]

        call_command("wait_for_db", stdout=StringIO())

        self.assertEqual(ensure_connection.call_count, 3)
        self.assertEqual(sleep.call_args_list, [call(1), call(1)])

    @patch("time.sleep")
    @patch(
        "django.db.backends.base.base.BaseDatabaseWrapper.ensure_connection"
    )
    def test_propagates_unexpected_errors(self, ensure_connection, sleep):
        ensure_connection.side_effect = ValueError("Invalid configuration")

        with self.assertRaisesMessage(ValueError, "Invalid configuration"):
            call_command("wait_for_db", stdout=StringIO())

        ensure_connection.assert_called_once_with()
        sleep.assert_not_called()
