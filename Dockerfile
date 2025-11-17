FROM python:3.13.0-alpine3.19
LABEL maintainer="bashyrov"

ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR app/

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir -p /files/media

RUN adduser \
    --disabled-password \
    --no-create-home \
    my_user

RUN chown -R my_user /files/media
RUN chmod -R 755 /files/media

COPY . .

USER my_user
