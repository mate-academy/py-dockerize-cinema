FROM python:3.11.4-slim-buster

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

RUN mkdir -p /vol/web/media
RUN adduser \
        --disabled-password \
        --no-create-home \
        django-user

COPY . .

RUN chown -R django-user:django-user /usr/src/app /vol/
RUN chmod -R 755 /vol/web/

USER django-user
