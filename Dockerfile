FROM python:3.9-alpine

WORKDIR /app

# Создаем пользователя
RUN adduser -D django-user

# Копируем файлы и устанавливаем зависимости
COPY requirements.txt .
RUN apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-build-deps \
        gcc libc-dev linux-headers postgresql-dev && \
    pip install -r requirements.txt && \
    apk del .tmp-build-deps

# Теперь создаем папки и меняем права
RUN mkdir -p /vol/web/media && \
    chown -R django-user:django-user /vol/ && \
    chmod -R 755 /vol/web/

# Переключаемся на этого пользователя
USER django-user