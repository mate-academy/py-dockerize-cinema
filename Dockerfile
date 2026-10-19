FROM python:3.12-slim
LABEL maintainer="idytkoni@gmail.com"

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    MEDIA_ROOT=/files/media \
    STATIC_ROOT=/files/static

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN adduser --disabled-password --no-create-home --gecos "" django-user \
    && mkdir -p /files/media /files/static \
    && chown -R django-user:django-user /files \
    && chmod -R 755 /files

USER django-user

EXPOSE 8000
