FROM python:3.11-slim
LABEL maintainer="your_email@example.com"

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p /vol/web/media /vol/web/static \
    && adduser --disabled-password --no-create-home django-user \
    && chown -R django-user:django-user /vol \
    && chmod -R 755 /vol

USER django-user

EXPOSE 8000