FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    MEDIA_ROOT=/vol/web/media \
    STATIC_ROOT=/vol/web/static

WORKDIR /app
COPY requirements-runtime.txt requirements.txt ./
ARG INSTALL_DEV=false
RUN pip install --no-cache-dir -r requirements-runtime.txt \
    && if [ "$INSTALL_DEV" = "true" ]; then \
        pip install --no-cache-dir -r requirements.txt; \
    fi \
    && adduser --disabled-password --gecos "" --uid 10001 django-user \
    && mkdir -p /vol/web/media /vol/web/static \
    && chown -R django-user:django-user /vol/web

COPY --chown=django-user:django-user . .
RUN chmod +x /app/docker-entrypoint.sh
USER django-user
EXPOSE 8000
ENTRYPOINT ["/app/docker-entrypoint.sh"]
CMD ["sh", "-c", "python manage.py migrate --noinput && python manage.py collectstatic --noinput && exec python manage.py runserver 0.0.0.0:8000 --noreload"]
