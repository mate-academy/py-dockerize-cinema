FROM python:3.11.3-alpine
LABEL maintainer="bilmaxim@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR /docker-cinema-app/

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN adduser --disabled-password --no-create-home django-user
RUN mkdir -p /vol/web/media
RUN chown -R django-user:django-user /vol/
RUN chmod -R 755 /vol/web/

USER django-user
