FROM python:3.10.4-slim-buster
LABEL mainteiner="maramorosh2@gmail.com"

ENV PYTHONUNBUFFERED 1 && WAIT_VERSION 2.7.2

WORKDIR app/

ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.10.0/wait /wait
RUN chmod +x /wait

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
