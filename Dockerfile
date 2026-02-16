FROM python:3.12-alpine3.23

WORKDIR /app

ENV PYTHONUNBUFFERED=1

COPY requirements.txt requirements.txt

RUN python -m pip install --upgrade pip && pip install -r requirements.txt

COPY . .

RUN mkdir -p /files/media

RUN adduser \
    --disabled-password \
    --no-create-home \
    custom_user

RUN chown -R custom_user /files/media
RUN chmod -R 0755 /files/media

USER custom_user
