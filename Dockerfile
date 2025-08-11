FROM python:3.12-slim
LABEL maintainer="bondziks@gmail.com"

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cashe-dir -r requirements.txt

COPY entrypoint.sh /app/
RUN chmod +x /app/entrypoint.sh

COPY . .
RUN mkdir -p /files/media

RUN adduser \
    --disabled-password \
    --no-create-home \
    my_user


RUN chown -R my_user /files/media
RUN chmod -R 755 /files/media

USER my_user
