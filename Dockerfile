FROM python:3.11-alpine

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

RUN apk add --no-cache \
    postgresql-client \
    jpeg-dev \
    zlib-dev \
    libjpeg

RUN apk add --no-cache --virtual .build-deps \
    gcc \
    musl-dev \
    postgresql-dev

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN apk del .build-deps

RUN adduser -D appuser

RUN mkdir -p /vol/web/media /vol/web/static && \
    chown -R appuser:appuser /vol

COPY --chown=appuser:appuser . .

USER appuser

EXPOSE 8000

CMD ["sh", "-c", "python manage.py wait_for_db && \
                  python manage.py migrate && \
                  python manage.py collectstatic --noinput && \
                  python manage.py runserver 0.0.0.0:8000"]
