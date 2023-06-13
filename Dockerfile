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

RUN useradd -rms /bin/zsh user_tm && chmod 777 /opt /run

WORKDIR /user_tm

RUN mkdir /user_tm/static && mkdir /user_tm/media && chown -R user_tm:user_tm /user_tm && chmod 755 /user_tm

COPY --chown=user_tm:user_tm . .

RUN pip install -r requirements.txt

USER user_tm

CMD ["gunicorn, '-b", "0.0.0.0:8000", "task_manager.wsgi:application"]

