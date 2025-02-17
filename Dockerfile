FROM python:3.10-slim
LABEL authors="fanni"

ENV PYTHOUNNBUFFERED 1

WORKDIR app/
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p /files/media

RUN adduser \
    --diasabled-password \
    --no-create-home \
    my_user

RUN chown -R my_user /files/media
RUN chmod -R 755 /files/media

USER my_user