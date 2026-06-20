FROM python:3.10-alpine3.18
LABEL maintainer="cinema-service"

ENV PYTHONUNBUFFERED=1

COPY requirements.txt /tmp/requirements.txt
COPY . /app
WORKDIR /app
EXPOSE 8000

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client jpeg-dev && \
    apk add --update --no-cache --virtual .tmp-build-deps \
        build-base postgresql-dev musl-dev zlib zlib-dev linux-headers && \
    /py/bin/pip install --no-cache-dir -r /tmp/requirements.txt && \
    apk del .tmp-build-deps && \
    rm -rf /tmp && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user && \
    mkdir -p /app/media /app/staticfiles && \
    chown -R django-user:django-user /app && \
    chmod -R 755 /app/media /app/staticfiles

ENV PATH="/py/bin:$PATH"

USER django-user
