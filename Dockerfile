FROM python:3.10.8-slim
LABEL maintainer="glov1eechess2@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p /files/media /files/static && \
    adduser --disabled-password --no-create-home django-user && \
    chown -R django-user /app /files/media /files/static && \
    chmod -R 755 /files/media /files/static

USER django-user

CMD python manage.py wait_for_db && \
    python manage.py migrate && \
    python manage.py runserver 0.0.0.0:8000
