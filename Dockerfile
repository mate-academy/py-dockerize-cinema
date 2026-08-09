FROM python:3.11.6-alpine3.18
LABEL maintainer="mr.denisyakubenko@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN adduser \
    --disabled-password \
    --no-create-home \
    my_user

RUN mkdir -p /files/media
RUN chown -R my_user /files/media
RUN chmod -R 755 /files/media

VOLUME ["/files/media"]

USER my_user

CMD [
"sh",
"-c",
"python manage.py wait_for_db && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
