FROM python:3.11
LABEL mainter="tkacuk2291@gmail.com"
ENV PYTHONBUFFERED 1

WORKDIR app/
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
