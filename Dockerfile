# Використовуємо офіційний образ Python 3.13.6-slim
FROM python:3.13.6-slim

# Встановлюємо змінну середовища, щоб Python не буферизував вивід
ENV PYTHONUNBUFFERED=1

# Створюємо робочу директорію в контейнері
WORKDIR /app/

# Копіюємо файл залежностей та встановлюємо їх
COPY requirements.txt .

RUN pip install -r requirements.txt

# Копіюємо всі файли проекту до робочої директорії
COPY . .

# Копіюємо наш entrypoint-скрипт та робимо його виконуваним
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# Встановлюємо entrypoint-скрипт як основну команду для контейнера
ENTRYPOINT ["/app/entrypoint.sh"]
