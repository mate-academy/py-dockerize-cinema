FROM python:3.10.15-alpine3.20

LABEL authors="mordegear90@gmail.com"

ENV PYTHONBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

RUN mkdir -p /vol/web/media

RUN adduser --disabled-password --no-create-home user_unit
RUN chown -R user_unit:user_unit /vol/
RUN chmod -R 755 /vol/web

USER user_unit
