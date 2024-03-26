FROM python:3.12.1-alpine
LABEL maintainer="oksanka.kot@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR cinema

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN adduser \
    --disabled-password \
    --no-create-home \
    my_user

RUN mkdir -p /files/media
RUN chown -R my_user /files/media
RUN chmod -R 755 /files/media

USER my_user
