FROM python:3.11.6-alpine3.18
LABEL maintainer="sandroahobadze@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apk add --no-cache \
    postgresql-dev gcc python3-dev musl-dev libffi-dev

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p /files/media /files/static

RUN adduser --disabled-password --no-create-home my_user
RUN chown -R my_user:my_user /files/media /files/static
RUN chmod -R 755 /files/media /files/static


USER my_user

CMD ["sh", "-c", "python manage.py wait_for_db && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
