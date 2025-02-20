FROM python:3.10

LABEL maintainer="galytskiyihor@gmail.com"

ENV PYTHONUNBUFFERED=1

RUN apt update && apt install -y dos2unix

WORKDIR /usr/src/requirements

COPY requirements.txt requirements.txt


RUN  python -m pip install --upgrade pip && \
     pip install --no-cache-dir -r requirements.txt

WORKDIR /usr/src/app

COPY ./src .

COPY ./commands /usr/src/commands

RUN dos2unix /usr/src/commands/*.sh