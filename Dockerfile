FROM python:3.11-alpine

ENV PYTHONUNBUFFERED=1

WORKDIR app/

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .
RUN mkdir -p /files/media

CMD sh -c "python manage.py wait_for_db && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"

RUN adduser \
    --disabled-password \
    --no-create-home \
    my_user

RUN chown -R my_user /files/media
RUN chmod -R 755 /files/media

USER my_user
