FROM python:3.10.14-alpine3.20

WORKDIR app

COPY . .

ENV PYTHONUNBUFFERED=1

RUN pip install -r requirements.txt
