FROM python:3.11-alpine

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p "/files/media"

RUN adduser \
    --disabled-password \
    --no-create-home \
    my_user

RUN chown -R my_user:my_user /files/media

RUN chown -R my_user:my_user /app

RUN chmod -R 755 /files/media

USER my_user
