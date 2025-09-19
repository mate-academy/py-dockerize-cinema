FROM python:3.13.7-slim
LABEL maintainer="maksbusl@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

RUN groupadd -r my_user_group && useradd --no-log-init -r -g my_user_group my_user

COPY . .

RUN mkdir -p /files/media
RUN mkdir -p /files/static

RUN chown -R my_user:my_user_group /files/media /files/static
RUN chmod -R 755 /files/media /files/static

USER my_user
