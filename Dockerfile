FROM python:3.12
LABEL maintainer="minkov215@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR app/

RUN pip install --no-cache-dir django psycopg2-binary gunicorn

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
RUN mkdir -p /files/media

RUN adduser \
    --disabled-password \
    --no-create-home \
    my_user

RUN chown -R my_user:my_user /files/media
RUN chmod -R 755 /files/media

USER my_user