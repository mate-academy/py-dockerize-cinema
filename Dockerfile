FROM python:3.13-slim
LABEL maintainer="KorJ4"

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN mkdir -p /vol/web/media /vol/web/static \
    && adduser \
        --disabled-password \
        --no-create-home \
        django-user \
    && chown -R django-user:django-user /vol/ \
    && chmod -R 755 /vol/web/

USER django-user
