FROM python:3.11.2-slim
LABEL maintainer="persie.iovchu@gmail.com"

ENV PYTHONBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt

RUN apt-get update && apt-get install -y gcc libpq-dev netcat-openbsd
RUN pip install -r requirements.txt

COPY . .

RUN mkdir -p /vol/web/media

RUN adduser \
         --disabled-password \
         --no-create-home\
         django-user

RUN chown -R django-user:django-user /vol/

RUN chown -R 755 /vol/web/

USER django-user
