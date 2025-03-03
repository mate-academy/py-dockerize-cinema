FROM python:3.11.11-slim

WORKDIR cinema/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN mkdir -p /files/media
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

RUN adduser \
    --disabled-password \
    --no-create-home \
    my_user
RUN chown -R my_user /files/media
RUN chmod -R 755 /files/media

USER my_user