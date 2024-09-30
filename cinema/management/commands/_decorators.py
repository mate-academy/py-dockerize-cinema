import time
from typing import Callable

import psycopg2


def reconnect(max_retries: int = 10, delay: int = 5) -> Callable:
    def decorator(func: Callable) -> Callable:
        def inner(*args, **kwargs) -> None:
            retries = 0
            while max_retries is None or retries < max_retries:
                try:
                    func(*args, **kwargs)
                    break
                except psycopg2.OperationalError:
                    retries += 1
                    print(
                        f"Database connection failed. Retry: "
                        f"{retries}/{max_retries}"
                    )
                    time.sleep(delay)
            else:
                print(
                    "Max retries exceeded. "
                    "Could not connect to the database."
                )

        return inner

    return decorator
