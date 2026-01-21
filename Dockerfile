FROM python:3.10-slim
LABEL maintainer="sofo4"

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p /app/vol/web/media && mkdir -p /app/vol/web/static

# Створюємо користувача для безпеки (опціонально, але рекомендовано)
# RUN adduser --disabled-password --no-create-home django-user
# RUN chown -R django-user:django-user /vol/
# RUN chmod -R 755 /vol/web/
# USER django-user

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
