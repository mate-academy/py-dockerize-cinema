FROM python:3.13-slim
LABEL authors="barsu"

WORKDIR /app
COPY requirements.txt requirements.txt

RUN apt-get update && apt-get install -y gcc \
    && pip install --no-cache-dir -r requirements.txt \
    && apt-get remove -y gcc && apt-get autoremove -y

COPY . .


