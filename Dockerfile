FROM python:3.12-slim
LABEL maintainer="irakirvas78@gmail.com"
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN mkdir -p /files/media
RUN adduser \
    --disabled-password \
    --no-create-home \
    django-user
RUN chown -R django-user /files/media
RUN chmod -R 755 /files/media
USER django-user
