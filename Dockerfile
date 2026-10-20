FROM python:3.14-slim
LABEL maintainer="zahargalusko9@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir -p /files/media/

RUN adduser \
    --disabled-password \
    --no-create-home \
    django-user

RUN chown -R django-user:django-user /files/media/
RUN chmod -R 755 /files/media/

USER django-user
COPY . .
