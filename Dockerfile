FROM python:3.11.9-alpine3.20
LABEL maintainer="thecombopunk@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR /app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN apk add --no-cache su-exec
RUN mkdir -p /files/media
RUN adduser --disabled-password --no-create-home my_user

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]