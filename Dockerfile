FROM python:3.10.0-slim-buster
LABEL maintainer="graanddadays@gmail.com"

WORKDIR app/

ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get -y install libpq-dev gcc

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

RUN mkdir -p /vol/web/media




COPY ./entrypoint.sh .
RUN sed -i "s/\r$//g" /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

COPY . .

ENTRYPOINT ["/app/entrypoint.sh"]

RUN mkdir -p /vol/app/media

RUN adduser \
    --disabled-password \
    --no-create-home \
    django-user

RUN chown -R django-user:django-user /vol/
RUN chmod -R 755 /vol/app/

USER django-user
