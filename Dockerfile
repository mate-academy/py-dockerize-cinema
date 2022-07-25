FROM python:3.10.4-alpine
LABEL maintainer="bohdankryven1@gmail.com"

ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE cinema_service.settings

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN mkdir -p /vol/web/media

RUN adduser \
    --disabled-password \
    --no-create-home \
    django-user

RUN chown -R django-user:django-user /vol/
RUN chmod -R 755 /vol/web/

USER django-user
