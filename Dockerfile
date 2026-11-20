FROM python:3.12-alpine3.18
LABEL maintainer="artemmurtazin27@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN mkdir -p /files/media

RUN adduser \
    -D -H \
    my_user

RUN chown -R my_user /files/media
RUN chmod -R 755 /files/media

USER my_user
