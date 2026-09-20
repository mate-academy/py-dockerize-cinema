FROM python:3.10.8-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod +x /app/wait_for_db.sh

EXPOSE 8000

CMD ["/app/wait_for_db.sh"]
