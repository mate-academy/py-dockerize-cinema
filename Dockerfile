FROM python:3.11-alpine
LABEL maintainer="student@mate.academy"

ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Установка зависимостей системы
RUN apk add --update --no-cache \
    postgresql-client \
    jpeg-dev \
    libc-dev \
    linux-headers \
    postgresql-dev \
    zlib-dev

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

# Создание папок для статики и медиа
RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static

# Безопасность: запуск от не-root пользователя
RUN adduser -D user
RUN chown -R user:user /vol/
RUN chmod -R 755 /vol/web
USER user