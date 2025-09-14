FROM python:3.12-slim
LABEL maintainer="mykola.makovynskyi@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p /media /static

RUN adduser \
    --disabled-password \
    --no-create-home \
    my_user

RUN chown -R my_user /media /static
RUN chmod -R 755 /media /static

USER my_user
