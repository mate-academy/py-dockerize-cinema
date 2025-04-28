FROM python:3.10-alpine3.18

ENV PYTHONBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

RUN adduser \
    --disabled-password \
    --no-create-home \
    django-user

RUN mkdir -p /vol/web/media

RUN chown -R django-user:django-user /vol/
RUN chmod -R 755 /vol/web/

RUN mkdir -p /vol/web/media

COPY . .
