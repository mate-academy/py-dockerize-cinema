FROM python:3.12-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN adduser \
        --disabled-password \
        --no-create-home \
        django-user && \
    mkdir -p /app/media /app/staticfiles && \
    chown -R django-user:django-user /app

COPY --chown=django-user:django-user . .

USER django-user

EXPOSE 8000