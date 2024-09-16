FROM python:3.12-alpine
LABEL maintainer="u123@ua.fm"

ENV PYTHONUNBUFFERED 1

WORKDIR app/

COPY requirements.txt ./
RUN pip install -r  requirements.txt
COPY . .

RUN mkdir -p /files/media

RUN adduser \
    --disabled-password\
    --no-create-home\
    me-user

RUN chown -R me-user /files/
RUN chmod -R 755 /files/media

USER me-user
