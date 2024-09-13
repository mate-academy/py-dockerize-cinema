LABEL maintainer="developer14062007@gmail.com"

ENV PYTHOUNNBUFFERED 1


WORKDIR app/

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
RUN mkdir -p /uploads/movies

RUN adduser \
    --disabled-password \
    --no-create-home\
    my_user

RUN chown -R my_user /uploads/movies
RUN chown -R 755 /uploads/movies

USER my_user
