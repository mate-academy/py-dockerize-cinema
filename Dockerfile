FROM python:3.10-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN adduser \
    --disabled-password \
    --no-create-home \
    django-user

COPY . .

RUN mkdir -p /vol/web/media
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN chown -R django-user:django-user /vol/
RUN chmod -R 755 /vol/web/

RUN python manage.py migrate

USER django-user
