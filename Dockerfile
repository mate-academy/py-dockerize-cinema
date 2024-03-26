FROM python:3.12-slim
LABEL maintainer="clarioruberia@gmail.com"

ENV PYTHONUNNBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .
