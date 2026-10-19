FROM python:3.14.0-slim
LABEL authors="fedir1357@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p /files/media &&  \
    mkdir -p /files/static &&  \
    adduser \
    --disabled-password \
    --no-create-home \
    my_user &&  \
    chown -R my_user /files &&  \
    chmod -R 755 /files

USER my_user