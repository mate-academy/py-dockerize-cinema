FROM python:3.9-slim-bullseye
LABEL maintainer="darkvader.ukr.net@gmail.com"

SHELL ["/bin/bash", "-c"]

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

EXPOSE 8000

RUN pip install --upgrade pip

RUN apt-get update && apt-get install -y \
    gcc \
    libjpeg-dev \
    libxslt-dev \
    libpq-dev \
    libmariadb-dev \
    libmariadb-dev-compat \
    gettext \
    cron \
    openssh-client \
    flake8 \
    locales \
    libpq-dev \
    postgresql-client

RUN useradd -rms /bin/zsh django_user && chmod 777 /opt /run

WORKDIR /django_user

RUN mkdir /django_user/static && mkdir /django_user/media && chown -R django_user:django_user /django_user && chmod 755 /django_user

COPY --chown=django_user:django_user . .

RUN pip install -r requirements.txt

USER django_user

CMD ["gunicorn, '-b", "0.0.0.0:8000", "cinema_service.wsgi:application"]

