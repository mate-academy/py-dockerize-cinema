FROM python:3.11.6-alpine3.18

ENV PYTHONUNBUFFERED 1

WORKDIR /cinema_service

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p /files/media /files/static

RUN adduser \
    --disabled-password \
    --no-create-home \
    my_user

RUN chown -R my_user /files
RUN chmod -R 755 /files

USER my_user