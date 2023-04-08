FROM python:3.10.8-slim
LABEL maintainer="vladysaf@gmail.com"

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]