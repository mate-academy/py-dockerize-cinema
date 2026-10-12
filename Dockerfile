FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

RUN addgroup --system django-user \
    && adduser --system --ingroup django-user django-user \
    && mkdir -p /vol/web/media /vol/web/static \
    && chown -R django-user:django-user /vol/web

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chown -R django-user:django-user /app

USER django-user

EXPOSE 8000

CMD ["sh", "-c", "python manage.py wait_for_db && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
