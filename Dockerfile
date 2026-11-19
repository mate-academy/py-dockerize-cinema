FROM python:3.15.2-alpine
LABEL author="Mateusz"

ENV PYTHONUNBUFFERED=1

WORKDIR /App


COPY requirements.txt .
RUN pip install -r requirements.txt

RUN adduser \
        --disabled-password \
        --no-create-home \
        django-user

COPY . .