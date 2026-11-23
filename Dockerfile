FROM python:3.12-slim

WORKDIR /cinema_service

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p /cinema_service/media /cinema_service/static

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]