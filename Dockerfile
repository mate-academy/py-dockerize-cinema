FROM python:3.11-alpine


ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


WORKDIR /app


COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt


COPY . .

RUN mkdir -p /app/media

EXPOSE 8000


CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
