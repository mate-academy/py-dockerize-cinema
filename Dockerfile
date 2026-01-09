FROM python:3.12-slim


ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN adduser \
    --disabled-password \
    --no-create-home \
    django-user

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static

RUN chown -R django-user:django-user /vol
RUN chmod -R 755 /vol

USER django-user
