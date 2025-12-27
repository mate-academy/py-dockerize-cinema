FROM python:3.12-alpine
LABEL maintainer="Konstantin-SVT"

WORKDIR app/

RUN pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN mkdir -p media

RUN adduser \
    --disabled-password \
    --no-create-home \
    secret-user

RUN chown -R secret-user media
RUN chmod -R 755 media

USER secret-user