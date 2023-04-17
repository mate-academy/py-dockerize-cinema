FROM python:3.10.6-slim
LABEL maintainer="zhukov9523@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .

RUN adduser \
    --disabled-password \
    --no-create-home \
    django-user

USER django-user
