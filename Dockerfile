FROM python:3.11.1-alpine

LABEL maintainer="olehoryshshuk@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR cinema_app/

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN mkdir -p /media

RUN adduser \
         --disabled-password \
         --no-create-home \
         cinema_user

RUN chown -R cinema_user:cinema_user /media/
RUN chmod -R 755 /media/

USER cinema_user
