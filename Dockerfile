FROM python:3.11.6-alpine3.18

LABEL maintainer="ananievvitalii10@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

RUN adduser --disabled-password --no-create-home my_user \
 && mkdir -p /app/media \
 && chown -R my_user:my_user /app/media

COPY . .

USER my_user

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
