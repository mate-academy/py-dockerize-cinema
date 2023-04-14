FROM python:3.11-slim
LABEL maintainer="ftftnvm2@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

RUN adduser \
    --disabled-password \
    --no-create-home \
    django-user \

RUN chown -R django-user:django-user /vol/
RUN chown -R 755 /vol/web/
RUN mkdir -p /vol/web/media

USER django-user