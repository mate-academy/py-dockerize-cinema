FROM python:3.10-alpine

ENV PYTHONUNBUFFERED 1

WORKDIR app/
COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir -p /files/media

RUN adduser --disabled-password --no-create-home my_user

RUN chown -R my_user /files/media
RUN chmod -R 755 /files/media # 755 читение запись и запуску, остальные не запись

USER my_user

COPY . .
