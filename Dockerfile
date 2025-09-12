FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt /app/
RUN apt-get update && apt-get install -y gcc libpq-dev && \
    pip install --no-cache-dir -r requirements.txt

COPY . /app/
RUN chmod +x /app/entrypoint.sh

CMD ["/app/entrypoint.sh"]
