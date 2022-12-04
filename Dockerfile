FROM python:3.10-alpine
LABEL maintainer="eugeneyakim4@google.com"

ENV PYTHONUNBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

RUN mkdir -p /vol/app/media

RUN adduser  \
    --disabled-password \
    --no-create \
    -home django-user

RUN chown -R django-user:django-user /vol/
RUN chmod -R 755 /vol/app/

USER django-user