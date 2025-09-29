FROM python:3.10.8-slim

LABEL mainteiner="lyubinska"

ENV PYTHONUNBUFFERED 1

WORKDIR cinema/

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt
COPY . .

RUN mkdir -p /files/media

RUN adduser \
    --disabled-password \
    --no-create-home \
    my_user

RUN shown -R my_user /files/media
RUN chmod -R 755 /files/media

USER my_user
