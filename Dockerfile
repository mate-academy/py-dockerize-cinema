FROM python:3.10.4-slim-buster

LABEL maintainer="ivan.korshunov.1997@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt

# install dependencies
RUN apt-get update \
    && apt-get -y install libpq-dev gcc

RUN pip install -r requirements.txt

COPY . .

RUN mkdir -p /vol/web/media

RUN adduser \
    --disabled-password \
    --no-create-home \
    django-user

# Give a permission to django-user to write info to this dirs
# In this particular case it allows me to save movie images to
# media dir (inside docker - vol/web/media)
RUN chown -R django-user:django-user /vol/
RUN chmod -R 755 /vol/web/

USER django-user
