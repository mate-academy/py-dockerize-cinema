FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p /files/media /files/static && \
    adduser --disabled-password --no-create-home my_user && \
    chown -R my_user /files/media /files/static && \
    chmod -R 755 /files

USER my_user

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
