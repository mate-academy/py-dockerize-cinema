FROM python:3.10.8-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

RUN mkdir -p /vol/web/media

CMD ["python ", "app/main.py"]
