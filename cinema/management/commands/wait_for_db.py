import os
import socket
import time

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Stop app before db isn`t done"""

    def handle(self, *args, **kwargs):
        port = int(os.environ["POSTGRES_PORT"])
        db_host = os.environ["POSTGRES_HOST"]
        db_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        while True:
            try:
                db_socket.connect((db_host, port))
                db_socket.close()
                break
            except socket.error:
                time.sleep(1)
