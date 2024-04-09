FROM python:3.11.6-alpine3.18
LABEL maintainer="evgeniy.playid@gmail.com"

ENV PYTHOUNBUFFERED 1
WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
RUN mkdir -p /files/media

RUN addgroup my_group && \
    adduser -D -H -S -G my_group my_user

RUN chown -R my_user /files/media
RUN chmod -R 755 /files/media

USER my_user
