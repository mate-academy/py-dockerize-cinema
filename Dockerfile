FROM python:3.10.12-slim-bullseye

LABEL maintainer='mykm3ua@gmail.com'

ENV PYTHONUNBUFFERED=1

WORKDIR app/

COPY . .

RUN pip install -r requirements.txt