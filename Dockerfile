FROM python:3.12-slim
LABEL maintainer="bohdanbrovdiy@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt 

COPY . .

RUN mkdir -p /vol/web/media

RUN adduser \
    --disabled-password \
    --no-create-home \
    cinema_user


RUN chown -R cinema_user:cinema_user /vol/
RUN chmod -R 755 /vol/web/


USER cinema_user
