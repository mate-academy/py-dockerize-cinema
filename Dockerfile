FROM python:3.10.12-slim

LABEL maintainer="roman.garmatiuk@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR app/

RUN mkdir -p /vol/web/media


COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .
RUN adduser \
    --disabled-password \
    --no-create-home \
    django-user

RUN chown -R django-user:django-user /vol/
RUN chmod -R 755 /vol/web/

USER django-user
