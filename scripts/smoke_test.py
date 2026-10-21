"""Exercise the running Compose app, then verify data after recreation."""
import base64
import json
import os
import sys
import time
from urllib.error import URLError
from urllib.request import Request, urlopen


BASE_URL = "http://127.0.0.1:8000"
MOVIES_URL = "/api/cinema/movies/"
IMAGE = base64.b64decode(
    "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAIAAACQd1PeAAAADElEQVR4nGNg"
    "YGAAAAAEAAH2FzhVAAAAAElFTkSuQmCC"
)


def request(path, data=None, token=None, content_type="application/json"):
    headers = {"Content-Type": content_type}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    with urlopen(Request(
        BASE_URL + path, data=data, headers=headers,
    ), timeout=10) as response:
        return response.read()


def main():
    for attempt in range(60):
        try:
            request("/api/cinema/")
            break
        except (URLError, ConnectionError, TimeoutError):
            if attempt == 59:
                raise
            time.sleep(1)

    credentials = json.dumps({
        "email": os.environ["DJANGO_SUPERUSER_EMAIL"],
        "password": os.environ["DJANGO_SUPERUSER_PASSWORD"],
    }).encode()
    token = json.loads(request("/api/user/token/", credentials))["access"]
    if sys.argv[1] == "create":
        movie = json.loads(request(MOVIES_URL, json.dumps({
            "title": "Docker persistence smoke test",
            "description": "Created by the Docker smoke test",
            "duration": 90,
        }).encode(), token))
        boundary = "cinema-smoke-boundary"
        payload = (
            f"--{boundary}\r\n"
            'Content-Disposition: form-data; name="image"; '
            'filename="smoke.png"\r\n'
            "Content-Type: image/png\r\n\r\n"
        ).encode() + IMAGE + f"\r\n--{boundary}--\r\n".encode()
        request(
            f"{MOVIES_URL}{movie['id']}/upload-image/", payload, token,
            f"multipart/form-data; boundary={boundary}",
        )

    movies = json.loads(request(MOVIES_URL, token=token))
    movie = next(
        item for item in movies
        if item["title"] == "Docker persistence smoke test"
    )
    image_path = movie["image"].removeprefix(BASE_URL)
    assert request(image_path) == IMAGE, "Uploaded media was not preserved"
    assert request("/static/rest_framework/css/bootstrap.min.css")
    print("API authentication, movie data, media, and static files verified.")


if __name__ == "__main__":
    main()
