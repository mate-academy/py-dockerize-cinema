ARG PYTHON_VERSION=3.12
FROM python:${PYTHON_VERSION}-slim AS base
LABEL maintainer="vlados.soc@gmail.com"

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p /files/media

RUN adduser \
    --disabled-password \
    --no-create-home \
    my_user

RUN chown -R my_user:my_user /files/media
RUN chmod -R 755 /files/media

USER my_user