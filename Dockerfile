FROM python:3.11.6-alpine3.18
LABEL maintainer="yaroslavsysoiev2000@gmail.com"

# Установка системных зависимостей
RUN apk add --no-cache gcc musl-dev jpeg-dev zlib-dev postgresql-dev

# Установка рабочего каталога
WORKDIR /app

# Копирование файла с зависимостями
COPY requirements.txt requirements.txt

# Установка зависимостей Python
RUN pip install --upgrade pip && pip install -r requirements.txt

# Копирование кода приложения
COPY . .

# Создание директории для медиа-файлов
RUN mkdir -p /files/media /files/static

# Настройка прав доступа для каталога файлов
RUN adduser -D my_user && \
    chown -R my_user /files/media /files/static && \
    chmod -R 755 /files/media /files/static

# Переключение на пользователя с ограниченными правами
USER my_user

# Команда по умолчанию
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
