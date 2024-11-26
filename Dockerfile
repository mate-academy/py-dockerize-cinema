FROM python:3.11.6-alpine3.18
LABEL maintainer="maksym.protsak@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR .

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "manage.py", "makemigrations"]
CMD ["python", "manage.py", "migrate"]
CMD ["python", "manage.py", "runserver"]
