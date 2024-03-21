FROM python:3.12-slim
LABEL maintainer="chebukin404@gmail.com"

WORKDIR cinema-mate/

ENV PYTHOUNNBUFFERED 1

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

RUN mkdir -p /files/media

RUN adduser \
    --disabled-password \
    --no-create-home \
    cinema_user

RUN chown -R cinema_user /files/media
RUN chmod -R 755 /files/media

USER cinema_user
