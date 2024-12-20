ARG PYTHON_VERSION=3.12.0
FROM python:${PYTHON_VERSION}-slim as base
LABEL maintainer="silva.vvss12@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR /cinema_service

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN mkdir -p /files/media
RUN adduser \
    --disabled-password \
    --no-create-home \
    my_user
RUN chown -R my_user /files/media
RUN chmod -R 755 /files/media

USER my_user

EXPOSE 8000

CMD gunicorn 'cinema_service.wsgi' --bind=0.0.0.0:8000
