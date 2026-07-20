FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static

EXPOSE 8000