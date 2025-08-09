FROM python:3.12-alpine
LABEL maintainer="volodymyrmyronets@gmail.com"

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR app/

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

RUN mkdir -p /files/media

RUN adduser \
        --disabled-password \
        --no-create-home \
        django_user

RUN chown -R django_user /files/media
RUN chmod -R 755 /files/media

USER django_user
