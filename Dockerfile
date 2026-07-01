FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && \
    apt-get install -y gcc libpq-dev && \
    pip install --upgrade pip && \
    pip install -r requirements.txt && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY . .

RUN mkdir -p /vol/web/static
RUN mkdir -p /vol/web/media

EXPOSE 8000

CMD sh -c "python manage.py wait_for_db && \
python manage.py migrate && \
python manage.py collectstatic --noinput && \
python manage.py runserver 0.0.0.0:8000"
