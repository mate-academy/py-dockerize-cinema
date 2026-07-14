FROM python:3.13-alpine
LABEL maintainer="andreygomenuk@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN mkdir -p /files/media /files/static

RUN adduser \
    --disabled-password \
    --no-create-home \
    my_user

RUN chown -R my_user /files/media /files/static
RUN chmod -R 755 /files/media /files/static

USER my_user
