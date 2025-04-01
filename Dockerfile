FROM python:3.11.11-alpine3.21

WORKDIR $APP_ROOT

COPY . $APP_ROOT

RUN pip install -r requirements.txt

RUN mkdir -p /files/media/
RUN mkdir -p /files/static/

RUN adduser \
    --disabled-password \
    --no-create-home \
    user

RUN chown -R user /files/
RUN chmod -R 755 /files/

USER user
