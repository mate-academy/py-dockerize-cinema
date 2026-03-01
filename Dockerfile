FROM python:3.12-alpine

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt


RUN apk add --no-cache --virtual .build-deps build-base postgresql-dev \
    && pip install --no-cache-dir -r requirements.txt \
    && apk del .build-deps

COPY . .

RUN mkdir -p /vol/web/media /vol/web/static

RUN adduser -D django-user && chown -R django-user /vol/web

USER django-user

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
