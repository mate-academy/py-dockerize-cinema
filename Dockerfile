FROM python:3.10.8-slim
LABEL maintainer="evgenijmartynuk07@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .



RUN adduser \
    --disabled-password \
    --no-create-home \
    django-user

RUN mkdir -p /vol/web/media/uploads/

RUN chown -R django-user:django-user /vol/web/media/uploads/
RUN chmod -R 755 /vol/web/media/uploads/

USER django-user
