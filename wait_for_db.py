import time
import psycopg2
from psycopg2 import OperationalError
import sys

def wait_for_db():
    while True:
        try:
            conn = psycopg2.connect(
                dbname=sys.argv[1],
                user=sys.argv[2],
                password=sys.argv[3],
                host=sys.argv[4]
            )
            conn.close()
            break
        except OperationalError:
            time.sleep(1)

if __name__ == '__main__':
    wait_for_db()
