FROM python:3.10
LABEL maintainer="derepovskiy98@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR app/

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

RUN mkdir -p /files/media #папка для медиа файлов

#создали нового юзера
RUN adduser \
    --disabled-password \
    --no-create-home \
    my_user

RUN chown -R my_user /files/media
RUN chmod -R 755 /files/media #чтение, запись и запуск для этого юзера

USER my_user