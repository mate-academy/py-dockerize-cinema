FROM python:3.10.12-slim-bullseye
LABEL maintainer="sasacihun4@gmail.com"

ENV PYTHOUNNBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
