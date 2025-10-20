FROM python:3.12-slim
LABEL maintainer="zhyharevk777.official@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y bash

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .


RUN mkdir -p /files/media /files/static \
    && adduser --disabled-password --no-create-home my_user \
    && chown -R my_user:my_user /files/media /files/static \
    && chmod -R 755 /files/media /files/static

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

USER my_user