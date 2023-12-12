import socket
import time
import os
from django.core.management.base import BaseCommand
from dotenv import load_dotenv


load_dotenv()


class Command(BaseCommand):
    BaseCommand.help = "Wait for DB to start before running server"

    def handle(self, *args, **options):
        port = int(os.environ["POSTGRES_DB_PORT"])

        bridge = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        while True:
            try:
                bridge.connect((os.environ["POSTGRES_HOST"], port))
                bridge.close()
                self.stdout.write("Connected!", ending="\n")
                break
            except socket.error:
                time.sleep(2)
