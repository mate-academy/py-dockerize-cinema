FROM python:3.13-slim
LABEL maintainer="prymak.olexandr@lll.kpi.ua"

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p /vol/web/media && \
    mkdir -p /vol/web/static && \
    useradd -ms /bin/bash django-user && \
    chown -R django-user:django-user /vol /app && \
    chmod -R 755 /vol

USER django-user
