from unittest.mock import patch

from django.core.management import call_command
from django.db import OperationalError
from django.test import SimpleTestCase


class WaitForDbTests(SimpleTestCase):
    @patch("cinema.management.commands.wait_for_db.time.sleep")
    @patch("django.db.backends.base.base.BaseDatabaseWrapper.ensure_connection")
    def test_database_available(self, connection, sleep):
        call_command("wait_for_db")

        connection.assert_called_once()
        sleep.assert_not_called()

    @patch("cinema.management.commands.wait_for_db.time.sleep")
    @patch("django.db.backends.base.base.BaseDatabaseWrapper.ensure_connection")
    def test_waits_until_database_available(self, connection, sleep):
        connection.side_effect = [OperationalError, OperationalError, None]

        call_command("wait_for_db")

        self.assertEqual(connection.call_count, 3)
        self.assertEqual(sleep.call_count, 2)
        sleep.assert_called_with(1)
