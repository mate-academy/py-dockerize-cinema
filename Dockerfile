FROM python:3.10.8-slim

WORKDIR app/

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY manage.py .
COPY cinema ./cinema
COPY cinema_service ./cinema_service
COPY user ./user
RUN mkdir -p /files/media /files/static

RUN adduser \
    --disabled-password \
    --no-create-home \
    my_user

RUN chown -R my_user /files/media
RUN chown -R my_user /files/static

RUN chmod -R 755 /files/media
RUN chmod -R 755 /files/static

USER my_user
