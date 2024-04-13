FROM python:3.11.6-alpine3.18

LABEL maintainer="adonos90@gmail.com"

ENV PYTHOUNNBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .
RUN mkdir -p /vol/dj-static/media

RUN adduser \
    --disabled-password \
    --no-create-home \
    usr

RUN chown -R usr:usr /vol/
RUN chown -R 755 /vol/dj-static/media

USER usr

