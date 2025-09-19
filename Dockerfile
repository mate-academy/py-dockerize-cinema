FROM python:3.10-alpine3.18
LABEL maintainer="orbik.rumlom22@gmail.com"

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

RUN apk add --no-cache --virtual .build-deps \
    postgresql-dev gcc python3-dev musl-dev

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt && \
    apk del .build-deps

COPY . .