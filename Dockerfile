FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential gcc libpq-dev libjpeg-dev zlib1g-dev curl && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN adduser --disabled-password --no-create-home django-user

RUN mkdir -p /vol/web/media && \
    chown -R django-user:django-user /vol && \
    chmod -R 755 /vol/web

COPY . /app
RUN chown -R django-user:django-user /app

USER django-user

EXPOSE 8000

CMD ["gunicorn", "cinema_service.wsgi:application", "--bind", "0.0.0.0:8000"]
