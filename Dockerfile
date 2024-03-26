FROM python:3.12-alpine
LABEL mainteiner="maksym.symonovych@gmail.com"

ENV PYTHOUNNBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN mkdir -p /files/media

RUN adduser \
    --disabled-password \
    --no-create-home \
    django-user

RUN chown -R django-user /files/media
RUN chmod -R 755 /files/media

USER django-user
