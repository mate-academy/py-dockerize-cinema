ARG PYTHON_VERSION=3.10
FROM python:${PYTHON_VERSION}-slim AS base
LABEL maintainer="vladislav.tmf@gmail.com"

# Prevents Python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1

# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code into the container.
COPY . /app/

# Create a non-privileged user that the app will run under.
# See https://docs.docker.com/go/dockerfile-user-best-practices/
ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/app" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    django-user

RUN mkdir -p /app/media \
    && chown -R django-user:django-user /app \
    && chmod -R 755 /app/media

# Switch to the non-privileged user to run the application.
USER django-user
