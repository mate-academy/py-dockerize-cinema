FROM python:3.11.14-slim-trixie
LABEL authors="v.nykonenko@gmail.com"

ENV PYTHONUNBUFFERED 1
WORKDIR app/

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p /files/media && \
    useradd -r -s /bin/false my_user && \
    chown -R my_user:my_user /files/media && \
    chmod -R 755 /files/media

USER my_user
