FROM python:3.10.12-slim-bullseye

LABEL maintainer='mykm3ua@gmail.com'

ENV PYTHONUNBUFFERED=1

WORKDIR app/

COPY . .

RUN pip install -r requirements.txt

RUN mkdir media

RUN adduser \
        --disabled-password \
        --no-create-home \
        django-user

RUN chown -R django-user media

RUN chmod -R 755 media

USER django-user
