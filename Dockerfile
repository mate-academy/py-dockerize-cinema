FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

RUN addgroup --system app && adduser --system --ingroup app app \
    && mkdir -p /vol/web/static /vol/web/media \
    && chown -R app:app /vol/web

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY --chown=app:app . .
USER app

EXPOSE 8000

CMD ["sh", "-c", "python manage.py wait_for_db && python manage.py migrate --noinput && python manage.py runserver 0.0.0.0:8000"]
