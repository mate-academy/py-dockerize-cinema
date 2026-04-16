FROM python:3.11-alpine
LABEL  maintainer="ys33ys33ys55@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR  /app/


COPY . .

RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir -p /files/media/

RUN adduser --disabled-password --no-create-home my_user

RUN chown -R my_user /files/media/
RUN chmod -R 755 /files/media/

USER my_user
