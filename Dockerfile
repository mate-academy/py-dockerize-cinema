FROM python:3.11
LABEL authors="zhyganiuk.elizaveta@gmail.com"

ENV PYTHONUNBUFFERED=1

RUN apt update && apt install -y dos2unix

WORKDIR /usr/src

COPY requirements.txt requirements.txt


RUN python -m pip install --upgrade pip && \
    pip install -r requirements.txt

WORKDIR /usr/src

COPY ./app .

COPY ./commands /usr/src/commands

RUN dos2unix /usr/src/commands/*.sh