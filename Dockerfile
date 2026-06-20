FROM python:3.11-alpine AS builder

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apk add --no-cache postgresql-dev gcc python3-dev musl-dev jpeg-dev zlib-dev

COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r requirements.txt


FROM python:3.11-alpine

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apk add --no-cache libpq jpeg-dev zlib-dev

COPY --from=builder /app/wheels /wheels
COPY --from=builder /app/requirements.txt .
RUN pip install --no-cache /wheels/*


COPY . .


RUN adduser --disabled-password --no-create-home django-user
RUN mkdir -p /vol/web/media /vol/web/static && \
    chown -R django-user:django-user /app /vol && \
    chmod -R 755 /vol

USER django-user
