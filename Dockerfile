FROM python:3.10.8-slim
LABEL maintainer = "tanyakozakova"

ENV PYTHONUNBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN mkdir -p /vol/web/media/uploads

RUN adduser \
    --disabled-password \
    --no-create-home \
    --gecos '' \
    django-user

RUN chown -R django-user:django-user /vol/

USER django-user
