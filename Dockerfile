FROM python:3.9.6-slim-buster

ENV PYTHONUNBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt


COPY . .

RUN mkdir -p /vol/web/media

RUN adduser \
    --disabled-password \
    --no-create-home \
    django_user

RUN chown -R django_user:django_user /vol/
RUN chmod -R 755 /vol/web/

USER django_user
