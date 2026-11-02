FROM python:3.15-alpine3.24

ENV PYTHONUNBUFFERED=1
WORKDIR app/

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .