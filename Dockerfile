FROM python:3.11.4-slim-buster
LABEL maintainer="adamchuk.oksana01.08@gmail.com"

WORKDIR app/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN mkdir -p /vol/web/media

RUN adduser \
    --disabled-password \
    --no-create-home \
    cinema-user

RUN chown -R cinema-user:cinema-user /vol/
RUN chmod -R 755 /vol/web/

USER cinema-user
