FROM python:3.10-alpine as builder

RUN apk add --no-cache \
    postgresql-dev \
    gcc \
    python3-dev \
    musl-dev \
    libffi-dev

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt


FROM python:3.10-alpine

LABEL maintainer="alexsotnikov"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PATH="/home/appuser/.local/bin:${PATH}"

COPY --from=builder /root/.local /home/appuser/.local
COPY --from=builder /usr/lib/postgresql* /usr/lib/postgresql/

RUN apk add --no-cache \
    libpq \
    && rm -rf /var/cache/apk/*

WORKDIR /app
COPY . .

RUN adduser -D appuser && \
    mkdir -p /vol/web/static /vol/web/media && \
    chown -R appuser:appuser /vol && \
    chmod -R 755 /vol && \
    chmod +x /app/entrypoint.sh

USER appuser

ENTRYPOINT ["/app/entrypoint.sh"]
