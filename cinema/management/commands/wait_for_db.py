import os
import socket
import time

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Displays stats related to Article and Comment models'

    @staticmethod
    def wait_for_db():
        port = int(os.environ["DB_PORT"])
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        while True:
            try:
                s.connect(("db", port))
                s.close()
                break
            except socket.error as _:
                time.sleep(0.1)
