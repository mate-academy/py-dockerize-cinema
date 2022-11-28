FROM python:3.10.8-alpine
LABEL maintainer=illia.vyplavin@gmail.com

ENV PYTHONUNBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt

RUN apk add --update --no-cache --virtual .tmp-build-deps \
        gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev
RUN pip install -r requirements.txt
RUN apk del .tmp-build-deps

COPY . .

RUN mkdir -p vol/web/media/

RUN adduser \
    --disabled-password \
    --no-create-home \
    cinema-service-user

RUN chown -R cinema-service-user:cinema-service-user vol/
RUN chmod -R 755 vol/web/

USER cinema-service-user

CMD ["ls", "-la"]
