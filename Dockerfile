FROM python:3.11.4-alpine
LABEL maintainer="volodymyr_dolgyi@ukr.net"

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

RUN mkdir -p /files/media

COPY . .

RUN adduser --disabled-password --no-create-home my_user && \
    chown -R my_user /files/media && \
    chmod -R 755 /files/media

USER my_user
