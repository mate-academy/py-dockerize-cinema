FROM python:3.11-slim

LABEL maintainer="malyshkoserhii91@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

RUN adduser \
    --disabled-password \
    --no-create-home \
    my_user && \
    mkdir -p /files/media && \
    chown -R my_user:my_user /files && \
    chmod -R 775 /files

USER my_user
