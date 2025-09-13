FROM python:3.10-slim
LABEL maintainer="taraskravetc28@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN apt-get update && \
    apt-get install -y libpq-dev gcc python3-dev build-essential && \
    rm -rf /var/lib/apt/lists/*

RUN pip install -r requirements.txt
COPY . .

RUN adduser \
    --disabled-password \
    --no-create-home \
    my_user

RUN mkdir -p /app/media /app/staticfiles
RUN chown -R my_user:my_user /app/media /app/staticfiles
RUN chmod -R 755 /app/media /app/staticfiles

USER my_user