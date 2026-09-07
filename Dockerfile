FROM python:3.11.6-alpine3.18
LABEL authors="jackson"

ENV PYTHONUNBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
RUN mkdir -p /app/media

RUN adduser \
    --disabled-password \
    --no-create-home \
    my_user

RUN chown -R my_user /app/media
RUN chmod -R 755 /app/media

USER my_user
