FROM python:3.9-slim-bullseye
LABEL maintainer="darkvader.ukr.net@gmail.com"

SHELL ["/bin/bash", "-c"]

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

EXPOSE 8000

RUN pip install --upgrade pip

RUN apt update && apt -qy install gcc libjpeg-dev libxslt-dev \
libpq-dev libmariadb-dev libmariadb-dev-compat gettext cron openssh-client flake8 locales

RUN useradd -rms /bin/zsh django-user && chmod 777 /opt /run

WORKDIR /django-user

RUN mkdir /django-user/static && mkdir /django-user/media && chown -R django-user:user_tm /django-user && chmod 755 /django-user

COPY --chown=django-user:django-user . .

RUN pip install -r requirements.txt

USER django-user

CMD ["gunicorn, '-b", "0.0.0.0:8000", "cinema_service.wsgi:application"]

