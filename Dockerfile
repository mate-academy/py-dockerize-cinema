FROM python:3.11.0-slim
LABEL maintainer="nekrjkeee@gmail.com"

ENV PYTHONBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR app/

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt


RUN pip install -r requirements.txt

COPY . .

RUN mkdir -p /vol/web/media


RUN adduser \
    --disabled-password \
    --no-create-home \
    django-user

RUN chown -R django-user:django-user /vol/
RUN chmod -R 755 /vol/web/

USER django-user
