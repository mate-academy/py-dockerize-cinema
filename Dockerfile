FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR app/


RUN apt-get update && apt-get install -y \
    libpq-dev gcc netcat-traditional \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt


COPY . .
RUN mkdir -p /files/media /vol/web/static

RUN adduser \
    --disabled-password \
    --no-create-home \
    my-user

RUN chown -R my-user:my-user /vol/
RUN chmod -R 755 /vol/web/

USER my-user
