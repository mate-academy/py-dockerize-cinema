FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

RUN adduser \
    --disabled-password \
    --no-create-home \
    django-user \
    && mkdir -p /app/media /app/staticfiles \
    && chown -R django-user:django-user /app/media /app/staticfiles

USER django-user

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
