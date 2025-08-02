# Используем официальный образ Python как базовый
FROM python:3.12-slim

# Устанавливаем переменные окружения
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Создаем рабочую директорию
WORKDIR /app

# Устанавливаем зависимости системы
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Копируем зависимости проекта
COPY requirements.txt .

# Устанавливаем зависимости Python
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Копируем остальные файлы проекта
COPY . .

# Команда по умолчанию (будет заменена в docker-compose)
CMD ["gunicorn", "cinema.wsgi:application", "--bind", "0.0.0.0:8000"]
