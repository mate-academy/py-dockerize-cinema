FROM python:3.11.1-alpine
LABEL maintainer = "kuznetsbog@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt

RUN apk --update add libxml2-dev libxslt-dev libffi-dev gcc \
     musl-dev libgcc openssl-dev curl
RUN apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev \
    tiff-dev tk-dev tcl-dev
RUN pip install -r requirements.txt

RUN mkdir -p /vol/web/media

COPY . .

RUN adduser \
    --disabled-password \
    --no-create-home \
    django-user

RUN chown -R django-user:django-user /vol/
RUN chmod -R 755 /vol/web/

USER django-user