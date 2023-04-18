FROM python:3.11.0-slim
LABEL maintainer="davidglusch@gmail.com"

ENV PYTHONBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .


RUN adduser \
    --disabled-password \
    --no-create-home \
    django-user


USER django-user
