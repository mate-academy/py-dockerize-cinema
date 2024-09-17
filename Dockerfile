FROM python:3.11.3-slim-buster

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY . /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "manage.py", "wait_for_db", "&&", "python", "manage.py", "migrate", "&&", "python", "manage.py", "runserver", "0.0.0.0:8000"]

