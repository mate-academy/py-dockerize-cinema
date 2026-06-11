FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p /vol/web/static /vol/web/media \
    && useradd -M django-user \
    && chown -R django-user:django-user /vol \
    && chmod -R 755 /vol

EXPOSE 8000

USER django-user
