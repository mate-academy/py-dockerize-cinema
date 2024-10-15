FROM python:3.12-alpine3.20
LABEL maintainer="apolitov83@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN apk add --no-cache bash  # Install bash

RUN adduser \
        --disabled-password \
        --no-create-home \
        my_user

# Create the /files/media directory
RUN mkdir -p /files/media

# Change ownership and permissions
RUN chown -R my_user /files/media
RUN chmod -R 755 /files/media

USER my_user
