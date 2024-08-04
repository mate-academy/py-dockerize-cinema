FROM python:3.11.9-alpine3.19
LABEL maintainer="clash2clans1one@gmail.com"

ENV PYTHOUNNBUFFERED 1

WORKDIR app/

COPY . .
RUN pip install -r requirements.txt
RUN mkdir -p /files/media

RUN adduser \
    --disabled-password \
    --no-create-home \
    my_user

RUN chown -R my_user /files/media
RUN chmod -R 755 /files/media

USER my_user