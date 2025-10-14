FROM python:3.11-slim
LABEL maintainer="viktoria.om@gmail.com"
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

RUN mkdir -p /files/media
RUN mkdir -p /app/static
RUN python manage.py collectstatic --noinput


RUN adduser \
    --disabled-password \
    --no-create-home \
    my_user

RUN chown -R my_user /files/media
RUN chmod -R 755 /files/media
RUN chown -R my_user /app/static

USER my_user
