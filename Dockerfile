FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p /files/media

RUN adduser --disabled-password --no-create-home my_user
RUN chown -R my_user /files/media
RUN chmod -R 755 /files/media
RUN mkdir -p /app/staticfiles
RUN chown -R my_user /app/staticfiles
RUN chmod -R 755 /app/staticfiles

USER my_user

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
