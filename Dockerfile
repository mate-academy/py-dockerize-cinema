FROM python:3.13.3-alpine3.21
LABEL maintainer="andriishtaher@gmail.com"

ENV PYTHONBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

RUN mkdir -p /app/media

RUN adduser \
    --disabled-password \
    --no-create-home \
    my_user

RUN chown -R my_user /app/media
RUN chmod -R 775 /app/media

USER my_user
