FROM python:3.11-slim
LABEL maintainer="allakhverdovyuriy@gmail.com"

ENV PYTHONBUFFERRED 1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]