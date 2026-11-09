FROM python:3.14-slim
LABEL maintainer="mate.academy"

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN mkdir -p /vol/web/media /vol/web/static \
    && adduser \
        --disabled-password \
        --no-create-home \
        --gecos "" \
        django-user \
    && chown -R django-user:django-user /vol \
    && chmod -R 755 /vol

USER django-user
