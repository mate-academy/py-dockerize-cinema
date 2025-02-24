FROM python:3.12.0-alpine3.18

LABEL maintainer="slradbez@gmail.com"

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]
