FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN adduser \
        --disabled-password \
        --no-create-home \
        django-user

RUN mkdir -p /vol/web/media /vol/web/static && \
    chown -R django-user:django-user /vol/ && \
    chmod -R 755 /vol/web/media /vol/web/static

USER django-user

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]