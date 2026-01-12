FROM python:3.12-alpine

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN adduser \
        --disabled-password \
        --no-create-home \
        django-user


RUN mkdir -p ./media
RUN chown -R django-user:django-user ./media
RUN chmod -R 755 ./media

USER django-user
