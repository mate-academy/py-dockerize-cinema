FROM python:3.12-slim
LABEL maintainer="mr.maddarknes@gmail.com"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY ./requirements.txt /tmp/requirements.txt
RUN pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt && \
    rm -rf /tmp

COPY . .

RUN mkdir -p /vol/web/media && \
    mkdir -p /vol/web/static && \
    adduser --disabled-password --no-create-home django-user && \
    chown -R django-user:django-user /vol/ && \
    chmod -R 755 /vol/

USER django-user