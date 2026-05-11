FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN adduser \
        --disabled-password \
        --no-create-home \
        django-user

RUN mkdir -p /vol/web/media /vol/web/static

RUN chown -R django-user:django-user /vol/
RUN chmod -R 755 /vol/web/

COPY --chown=django-user:django-user . .

USER django-user

CMD manage.py runserver 0.0.0.0:8000