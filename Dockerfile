FROM python:3.9-slim

WORKDIR /py-dockerize-cinema

COPY . .

RUN pip install -r requirements.txt

RUN adduser --disabled-password --no-create-home django-user

RUN mkdir -p /vol/web/media

USER django-user

CMD ["sh", "-c", "python manage.py wait_for_db && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]


