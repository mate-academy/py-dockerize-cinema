# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR app/

# Install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt


COPY . .


RUN mkdir -p /files/media
RUN mkdir -p /files/static
RUN adduser \
         --disabled-password \
         --no-create-home \
         django-user

RUN chown -R django-user /files/media
RUN chmod -R 755 /files/media
RUN chown -R django-user /files/static
RUN chmod -R 755 /files/static
USER django-user


