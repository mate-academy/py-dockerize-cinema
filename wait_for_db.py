import time
import psycopg2
from psycopg2 import OperationalError


def wait_for_db():
    while True:
        try:
            conn = psycopg2.connect(
                dbname="cinema",
                user="user",
                password="password",
                host="db",
                port="5432"
            )
            conn.close()
            print("Database is ready!")
            break
        except OperationalError:
            print("Waiting for database...")
            time.sleep(3)


if __name__ == "__main__":
    wait_for_db()
