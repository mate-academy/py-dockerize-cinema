FROM python:3.11

WORKDIR /cinema

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN adduser --disabled-password --no-create-home my_user

COPY . .

RUN mkdir -p /files/media

RUN chown -R my_user /files/media
RUN chmod -R 755 /files/media

USER my_user

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
