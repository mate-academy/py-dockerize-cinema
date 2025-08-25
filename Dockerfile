FROM  python:3.11.6-alpine3.18
LABEL maintainer="olgashumska65@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN mkdir -p /files/media

RUN mkdir -p /files/static

RUN adduser \
    --disabled-password\
    --no-create-home\
    my_user

RUN chown -R my_user /files/media
RUN chmod -R 755 /files/media

RUN chown -R my_user /files/static
RUN chmod -R 755 /files/static

USER my_user
