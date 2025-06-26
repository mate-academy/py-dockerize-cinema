FROM python:3.12-slim
LABEL maintainer="smolinskijmaksim@gmail.com"

ENV PYTHONUNBUFFERED 1

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
RUN mkdir -p /files/media && \
    adduser \
    --disabled-password \
    --no-create-home \
    my_user && \
    chown -R my_user:my_user /files && \
    chmod -R 755 /files

USER my_user