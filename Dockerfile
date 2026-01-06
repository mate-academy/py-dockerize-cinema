FROM python:3.11.14-alpine3.21

ENV PYTHONUNBUFFERED=1

WORKDIR cinema/

COPY requirements.txt req.txt
RUN pip install -r req.txt

COPY . .
