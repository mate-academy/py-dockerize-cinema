FROM python:3.11.6-alpine3.18

ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN adduser \
    --disabled-password \
    --no-create-home \
    django-user

RUN mkdir -p /app/media \
    && chown -R django-user:django-user /app \
    && chmod -R 755 /app/media \

USER django-user