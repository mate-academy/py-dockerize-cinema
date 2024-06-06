FROM python:3.10

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p /files/media/

RUN adduser \
    --disabled-password \
    --no-create-home \
    my_user

RUN chown -R my_user /files/media
RUN chmod -R 755 /files/media

USER my_user



#RUN mkdir -p /vol/web/static
#
#RUN mkdir -p /vol/web/media
#
#ENV STATIC_ROOT=/vol/web/static
#ENV MEDIA_ROOT=/vol/web/media
#
#ENTRYPOINT ["sh", "-c", "python manage.py wait_for_db && gunicorn cinema.wsgi:application --bind 0.0.0.0:8000"]
