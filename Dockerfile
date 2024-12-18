FROM python:3.11.1

WORKDIR /cinema

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN adduser --disabled-password --no-create-home my_user && \
    mkdir -p /files/media && \
    chown -R my_user /files/media && \
    chmod -R 755 /files/media

COPY . .

USER my_user

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
