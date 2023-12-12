FROM python:3.11-slim-buster
LABEL maintainer="edlrian814@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR app/

RUN apt-get update -y \
    && apt-get install libpq-dev gcc -y

RUN pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN mkdir -p /vol/web/media

RUN adduser \
    --disabled-password \
    --no-create-home \
    django-user

RUN chown -R django-user:django-user /vol/
RUN chmod -R 755 /vol/web/

USER django-user
