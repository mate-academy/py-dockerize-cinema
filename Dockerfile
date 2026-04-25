FROM python:3.12.1-alpine3.18
LABEL maintainer="knyrikkolesnichenko2004@gmail.com"

WORKDIR app/

ENV PYTHONBUFFERED 1

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN mkdir -p /files/media/

RUN adduser \
    --disabled-password \
    --no-create-home \
    django_user

RUN chown -R django_user /files/media
RUN chmod -R 755 /files/media

USER django_user
