FROM python:3.12.1-slim
LABEL maintainer="ilaruslanovich7@gmail.om"

ENV PYTHOUNNBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt

RUN apt-get update && apt-get install -y \
    zlib1g-dev \
    build-essential \
    libjpeg-dev \
    libpng-dev \
    libtiff-dev \
    libwebp-dev \
    python3-dev\
    libpq-dev \
    gcc \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*



RUN pip install -r requirements.txt


COPY . .

RUN mkdir -p /files/media

RUN adduser \
    --disabled-password \
    --no-create-home \
    my_user

RUN chown -R my_user /files/media
RUN chmod -R 755 /files/media

USER my_user