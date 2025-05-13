FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt ./

#RUN python -m pip install --upgrade pip setuptools wheel
#RUN apt-get update && apt-get install -y \
#    libjpeg-dev \
#    zlib1g-dev \
#    libtiff-dev \
#    libfreetype6-dev \
#    gcc
RUN python -m pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

RUN adduser \
        --disabled-password \
        --no-create-home \
        django-user

