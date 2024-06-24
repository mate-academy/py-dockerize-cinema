FROM python:3.12-alpine
LABEL maintainer="d.villarionovich@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
RUN mkdir -p /media_files/upload


RUN adduser \
         --disabled-password \
         --no-create-home \
         django-user

RUN chown -R django-user:django-user /vol/
RUN chmod -R 755 /media_files

USER django-user