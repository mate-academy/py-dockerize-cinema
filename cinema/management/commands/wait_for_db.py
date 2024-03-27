import socket

from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):

    def handle(self, *args, **options):
        print("Waiting for DB")
        try:
            check_socket = socket.create_connection(("db", 5432), 5)
            check_socket.close()
            self.stdout.write(
                self.style.SUCCESS("DB runs successfully")
            )
            return
        except socket.error as e:
            print(e)

        raise CommandError("DB doesn't exist")
