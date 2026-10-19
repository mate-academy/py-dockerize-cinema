FROM python:3.12-alpine

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN adduser \
        --disabled-password \
        --no-create-home \
        my_user \
    && mkdir -p /vol/web/media /vol/web/static \
    && chown -R my_user:my_user /vol/web

COPY --chown=my_user:my_user . .

USER my_user
