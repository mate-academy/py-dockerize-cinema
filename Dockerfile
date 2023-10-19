FROM python:3.11.3-alpine

WORKDIR /code/

RUN mkdir -p /vol/web/media/

# create django-user that will have rwx
# permissions on /vol directory
RUN adduser --disabled-password \
  --no-create-home django-user

RUN chown -R django-user:django-user /vol
RUN chmod -R 755 /vol

COPY requirements.txt ./
# install necessary packages to work with postgresql
RUN apk add --update --no-cache postgresql-client jpeg-dev
RUN apk add --update --no-cache --virtual .tmp-build-deps \ 
  gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev
RUN pip install -r ./requirements.txt
RUN apk del .tmp-build-deps

ENV PYTHONUNBUFFERED=1

COPY . .
