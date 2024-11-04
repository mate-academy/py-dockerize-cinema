FROM python:3.10-alpine
LABEL maintainer="posseydon87@gmail.com"

ENV PYTHONBUFERRED 1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
RUN mkdir -p files/media files/staticfiles

