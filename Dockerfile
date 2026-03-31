FROM python:3.12-alpine
LABEL maintainer="dmitriykuzmin@ymail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN mkdir -p /files/media

RUN adduser \
    --disabled-password \
    --no-create-home \
    my_user

RUN chown -R my_user /files/media /app
RUN chmod -R 755 /files/media/

USER my_user
