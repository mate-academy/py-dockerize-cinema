FROM python:3.13-alpine
LABEL maintainer="volodymyr.vinohradov@gmail.com"

ENV PYTHONUNBUFFERED=1
ENV UV_PROJECT_ENVIRONMENT="/usr/local/"

WORKDIR /app
COPY pyproject.toml uv.lock ./

RUN pip install --no-cache-dir uv \
    && uv --no-cache-dir sync \
    && pip uninstall -y pip setuptools wheel uv \
    && rm -rf /root/.cache /root/.pip

COPY . .

RUN adduser --disabled-password --no-create-home my_user && \
    mkdir -p /files/media && \
    chown -R my_user /files/media && \
    chmod -R 755 /files/media

RUN chmod +x entrypoint.sh

ENTRYPOINT ["sh", "entrypoint.sh"]