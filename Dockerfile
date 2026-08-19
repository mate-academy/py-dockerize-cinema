FROM python:3.10.8-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

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

CMD ["sh", "-c", "python manage.py wait_for_db && python manage.py migrate && python manage.py collectstatic --noinput && python manage.py runserver 0.0.0.0:8000"]
