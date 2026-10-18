FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/opt/venv/bin:$PATH"

WORKDIR /app

RUN python -m venv /opt/venv
COPY requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

RUN groupadd --gid 10001 django \
    && useradd --uid 10001 --gid django --no-create-home django \
    && mkdir -p /vol/web/media /vol/web/static \
    && chown -R django:django /vol/web

COPY --chown=django:django . .

USER django
EXPOSE 8000

CMD ["sh", "-c", "python manage.py wait_for_db && python manage.py migrate --noinput && python manage.py collectstatic --noinput && python manage.py runserver 0.0.0.0:8000"]
