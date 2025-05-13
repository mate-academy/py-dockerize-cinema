FROM python:3.12-slim

# Встановлюємо залежності для psycopg2
RUN apt-get update && apt-get install -y \
    postgresql-client \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Встановлюємо робочу директорію
WORKDIR /app

# Встановлюємо залежності Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копіюємо код проекту
COPY . .

# Створюємо директорії для медіа та статичних файлів
RUN mkdir -p /app/media /app/static

# Створюємо користувача без прав root
RUN useradd -m appuser && chown -R appuser:appuser /app
USER appuser

# Запускаємо команду очікування бази даних та запуск сервера
CMD ["sh", "-c", "python manage.py wait_for_db && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"] 