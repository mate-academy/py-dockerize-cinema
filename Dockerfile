FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt /app/
RUN apt-get update && apt-get install -y gcc libpq-dev
RUN apt-get install -y --no-install-recommends gcc libpq-dev bash
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/
RUN chmod +x /app/entrypoint.sh
