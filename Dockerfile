FROM python:3.11-slim
LABEL maintainer="oleksii@example.com"

ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    zlib1g-dev \
    libjpeg-dev \
    && rm -rf /var/lib/apt/lists/*

RUN adduser --disabled-password \
    --no-create-home \
    django-user

RUN mkdir -p /vol/web/media
RUN chown -R django-user:django-user /vol/web

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


