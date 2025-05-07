FROM python:3.10-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Створюємо нового користувача для запуску додатка
RUN adduser --disabled-password --no-create-home app

# Створюємо необхідні директорії для медіа та статичних файлів
RUN mkdir -p /app/media /app/static
# Встановлюємо права доступу до директорій
RUN chown -R app:app /app

USER app 