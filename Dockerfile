FROM python:3.11-slim
LABEL maintainer="shulgadmytro3@gmail.com"

ENV PYTHONUNBUFFERED=1

RUN adduser \
    --disabled-password \
    --no-create-home \
    my_user

WORKDIR /app

RUN pip install --upgrade pip

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY --chown=my_user:my_user . .
RUN mkdir -p /files/media && chown -R my_user /files/media

USER my_user
