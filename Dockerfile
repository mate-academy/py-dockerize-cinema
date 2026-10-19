FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN mkdir -p /vol/web/media /vol/web/static \
    && useradd --no-create-home django-user \
    && chown -R django-user:django-user /vol/ \
    && chmod -R 755 /vol/web/

USER django-user

EXPOSE 8000
