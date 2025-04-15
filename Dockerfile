FROM python:3.10.0-slim
LABEL maintainer="slavuch232355@gmail.com"

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN adduser \
    --disabled-password \
    --no-create-home \
    my_user

USER my_user
