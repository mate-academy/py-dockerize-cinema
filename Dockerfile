FROM python:3.10.14-alpine3.20
LABEL maintainer="dmytroshchoma@gmail.com"

WORKDIR app/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .
RUN mkdir -p /vol/web/media

RUN adduser \
         --disabled-password \
         --no-create-home \
         my_user

RUN chown -R my_user:my_user /vol/web/media
RUN chmod -R 755 /vol/web/media

USER my_user
