FROM python:3.13.3-alpine AS init-stage
WORKDIR /app
COPY ./requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

FROM python:3.13.3-alpine AS entry-stage
WORKDIR /app
COPY --from=init-stage /install /usr/local
COPY . .

RUN rm -f requirements.txt
