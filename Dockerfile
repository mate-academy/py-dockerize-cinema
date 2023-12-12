FROM python:3.8.18-alpine
LABEL maintainer="chemuranov@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR /app/

COPY requirements.txt requirements.txt

RUN apk update && apk add -u libpq-dev gcc

RUN apk add -u zlib-dev jpeg-dev gcc musl-dev

RUN pip install -r requirements.txt

RUN mkdir -p /vol/web/media

COPY . .

RUN adduser --disabled-password --no-create-home django-user

COPY --chmod=755 entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

USER django-user
