FROM python:3.12-alpine
LABEL mainteiner="maksym.symonovych@gmail.com"

ENV PYTHOUNNBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN mkdir -p /vol/web/media

RUN adduser \
        --disabled-password \
        --no-create-home \
        django-user

RUN chown -R django-user /vol/web/media
RUN chown -R 755 /vol/web/media

USER djnago-user
