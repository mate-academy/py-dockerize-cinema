FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN mkdir -p files/media

RUN adduser \
    --disabled-password \
    --no-create-home \
    my_user \

RUN chown -R my_user files/media
RUN chmod -R u+w files/media

USER my_user
