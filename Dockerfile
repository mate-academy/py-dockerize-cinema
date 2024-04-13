FROM python:3.11.6-alpine3.18

LABEL maintainer="adonos90@gmail.com"

ENV PYTHOUNNBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .
RUN mkdir -p /vol/web/media

RUN adduser \
    --disabled-password \
    --no-create-home \
    user-dj

RUN chown -R user-dj /vol/
RUN chown -R 755 /vol/web

USER user-dj

