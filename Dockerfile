FROM python:3.11-slim
LABEL maintainer="antonbliznuk71@gmail.com"

RUN adduser \
        --disabled-password \
        --no-create-home django-user

WORKDIR /app
RUN mkdir -p /vol/web/media

RUN chown -R django-user:django-user /vol/
RUN chmod -R 755 /vol/web/


COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
ENV PYTHONUNBUFFERED=1
