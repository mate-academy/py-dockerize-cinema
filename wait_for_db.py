import time

import psycopg2

from cinema_service import settings


def wait_for_db():
    while True:
        try:
            conn = psycopg2.connect(
                host=settings.DATABASES["default"]["HOST"],
                port=settings.DATABASES["default"]["PORT"],
                dbname=settings.DATABASES["default"]["NAME"],
                user=settings.DATABASES["default"]["USER"],
                password=settings.DATABASES["default"]["PASSWORD"],
            )
            conn.close()
            print("DB доступна, всё ок!")
            break
        except psycopg2.OperationalError:
            print("Жду DB...")
            time.sleep(2)
