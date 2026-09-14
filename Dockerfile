FROM python:3.12
LABEL maintainer="Fabio Silva"

ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN adduser --disabled-password --no-create-home runtime

RUN mkdir -p /app/media/
RUN chown -R runtime /app/media/
RUN chmod -R 755 /app/media/

USER runtime
