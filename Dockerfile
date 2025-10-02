# ====== builder ======
FROM python:3.12-slim AS builder

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --upgrade pip \
    && pip wheel --wheel-dir /wheels -r requirements.txt


# ====== final ======
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# usuário não-root
RUN adduser --disabled-password --no-create-home django-user

WORKDIR /app

# libs de runtime
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq5 \
    && rm -rf /var/lib/apt/lists/*

# instalar deps via wheels
COPY --from=builder /wheels /wheels
RUN pip install --no-cache-dir /wheels/*

# copiar código (inclui entrypoint.sh) com propriedade correta
COPY --chown=django-user:django-user . .

# preparar volumes e entrypoint
RUN mkdir -p /vol/web/media /vol/web/static \
    && chown -R django-user:django-user /vol ./entrypoint.sh \
    && chmod +x ./entrypoint.sh \
    && chmod -R 755 /vol

USER django-user

# ENTRYPOINT: sempre esperar o DB antes do comando
ENTRYPOINT ["./entrypoint.sh"]

# CMD: migra, coleta estáticos e inicia o servidor
CMD ["sh", "-c", "python manage.py migrate && python manage.py collectstatic --noinput && python manage.py runserver 0.0.0.0:8000"]
