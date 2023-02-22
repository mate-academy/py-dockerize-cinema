# Cinema REST API
This project provides a RESTful API for managing various aspects of a cinema, including movies, actors, genres, cinema halls, movie sessions and orders. It comes with documentation and is Dockerized for easy deployment on any platform, making it ideal for both cinemas and developers building applications on top of the cinema's data.

## Installation
Python3 must be already installed
```shell
git clone https://github.com/GeorgePavlej/cinema-service-api.git
cd cinema-service-api
python -m venv venv
venv\Scripts\activate (Windows) or source venv/bin/activate (Linux or macOS)
pip install -r requirements.txt
copy .env.sample -> .env and populate with all required data
```

## Run migrations and server:

```shell
python manage.py migrate
python manage.py runserver
```
## Getting access
<hr>

- Create user via/api/user/register/
- Get access token via/api/user/token/

## You can run project using Docker container
<hr>

Docker must be already installed

```shell
docker-compose build
docker-compose up
```
## API documentation

The API documentation is available at:
- api/doc/swagger/
- api/doc/redoc/