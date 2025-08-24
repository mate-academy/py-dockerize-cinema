FROM python:3.11-alpine3.21

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN addgroup -S appgroup && adduser -S -G appgroup appuser

RUN mkdir -p /app/media /app/static && \
    chown -R appuser:appgroup /app/media /app/static

COPY --chown=appuser:appgroup requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY --chown=appuser:appgroup . .

USER appuser

EXPOSE 8000

CMD python manage.py wait_for_db && \
    python manage.py migrate && \
    python manage.py runserver 0.0.0.0:8000
