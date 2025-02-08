FROM python:3.11.11-slim
LABEL maintainer="zaharsavchen@gmail.com"

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt --no-cache-dir

COPY . .

RUN mkdir -p /vol/web/media && \
    mkdir /vol/web/static && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user && \
    chown -R django-user /vol/web/media && \
    chmod -R 755 /vol/web/media

USER django-user
