FROM python:3.12-slim-bullseye
LABEL maintainer="suskyivolodymyr@gmial.com"

ENV PYTHONUNBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
RUN mkdir ./media

RUN adduser \
    --disabled-password \
    --no-create-home \
    my_user

RUN chown -R my_user ./media
RUN chmod -R 755 ./media

USER my_user
