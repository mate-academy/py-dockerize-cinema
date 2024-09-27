FROM python:3.10.8-slim
LABEL maintainer="anonimchik920@gmail.com"

ENV PYTHOUNNBUUFFERED 1

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
