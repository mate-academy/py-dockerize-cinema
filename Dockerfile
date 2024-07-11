FROM python:3.11-alpine3.18
LABEL maintainer="annalepiska@gmail.com"

ENV PYTHOUNBUFFERED 1

WORKDIR app/

COPY . .
RUN mkdir -p /files/media

RUN pip install -r requirements.txt

RUN adduser \
         --disabled-password \
         --no-create-home \
         my-user

RUN chown -R my-user /files/media
RUN chmod -R 755 /files/media
