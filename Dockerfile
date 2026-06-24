FROM python:3.12-alpine

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .

RUN apk add --no-cache \
    postgresql-client \
    build-base \
    postgresql-dev

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static

CMD ["sh", "-c", "python manage.py wait_for_db && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
