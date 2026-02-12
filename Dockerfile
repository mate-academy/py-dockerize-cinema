FROM python:3.11-alpine
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Спочатку копіюємо файл зі списком бібліотек
COPY requirements.txt .

# Тепер запускаємо об'єднану команду інсталяції та очищення
RUN apk add --update --no-cache \
    postgresql-client \
    jpeg-dev \
    zlib-dev \
    libpq && \
    apk add --update --no-cache --virtual .tmp-build-deps \
    gcc \
    libc-dev \
    linux-headers \
    postgresql-dev \
    musl-dev \
    zlib-dev && \
    pip install --no-cache-dir -r requirements.txt && \
    apk del .tmp-build-deps

# Копіюємо решту коду
COPY . .

# Створюємо папки для статики та медіа
RUN mkdir -p /vol/web/media /vol/web/static