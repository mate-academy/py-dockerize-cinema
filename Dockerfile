FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

RUN mkdir -p /app/media/uploads/movies /app/staticfiles \
    && adduser --disabled-password --no-create-home my_user \
    && chown -R my_user:my_user /app \
    && chmod +x /app/entrypoint.sh


USER my_user

ENTRYPOINT ["/app/entrypoint.sh"]
