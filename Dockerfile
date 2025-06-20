FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /app/

RUN python manage.py collectstatic --noinput

CMD ["sh", "-c", "python manage.py wait_for_db && python manage.py runserver 0.0.0.0:8000"]
