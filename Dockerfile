FROM python:3.12.2-alpine
LABEL maintainer="pythonzem@gmail.com"

ENV PYTHONUNNBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

RUN mkdir -p /files/media

RUN adduser \
    --disabled-password \
    --no-create-home \
    test_user

RUN chown -R test_user /files/media
RUN chmod -R 755 /files/media


USER test_user