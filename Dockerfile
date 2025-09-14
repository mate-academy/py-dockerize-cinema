FROM python:3.10-alpine3.22
LABEL maintainer="pashock1337@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN apk add --no-cache postgresql-client && \
    pip install --no-cache-dir -r requirements.txt

RUN mkdir -p /files/media /files/static && \
    adduser -D -H django-user && \
    chown -R django-user /files/media /files/static && \
    chmod -R 755 /files/media /files/static

COPY . .

USER django-user

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
