FROM python:3.11.6-alpine3.18 AS builder
LABEL maintainer=freepgvlad@gmail.com

WORKDIR /app

RUN apk update && \
    apk add --no-cache \
    gcc \
    python3-dev \
    musl-dev \
    postgresql-dev

COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

FROM python:3.11.6-alpine3.18 AS final

RUN apk update && \
    apk add --no-cache libpq

WORKDIR /app

COPY --from=builder /usr/local/lib/python3.11/site-packages/ /usr/local/lib/python3.11/site-packages/

COPY . .

ENV PYTHONUNBUFFERED=1

COPY ./scripts/entrypoint.sh /usr/local/bin/entrypoint.sh

RUN mkdir -p /vol/web/media \
           /vol/web/static && \
    adduser -D my_user && \
    chown -R my_user:my_user /vol/web/media \
                             /vol/web/static && \
    apk add --no-cache sed && \
    sed -i 's/\r$//g' /usr/local/bin/entrypoint.sh && \
    chmod +x /usr/local/bin/entrypoint.sh && \
    apk del sed

EXPOSE 8000

USER my_user

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]