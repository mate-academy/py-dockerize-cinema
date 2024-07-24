FROM python:3.11.6-alpine3.18
LABEL maintainer="haldaniko@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt

RUN apk add --no-cache gcc musl-dev libpq-dev && \
    pip install --no-cache-dir -r requirements.txt && \
    apk del gcc musl-dev

COPY . .

RUN mkdir -p /vol/web/media

RUN adduser --disabled-password --no-create-home my_user

RUN chown -R my_user /vol/web/media
RUN chmod -R 755 /vol/web/media

USER my_user
