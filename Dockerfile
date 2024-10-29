FROM python:3.12-slim
LABEL maintainer="andri195595@gmail.com"

ENV PYTHOUNNBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
