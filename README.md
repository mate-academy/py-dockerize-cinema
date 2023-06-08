## Cinema API

This is a simple API for a cinema service. It is written in Python using the Django REST Framework.

### Features

- JWT authenticated;
- Admin panel;
- Documentation for endpoints is located at /api/doc/swagger/;
- Managing orders and tickets;
- Filtering movies and movie sessions.
- Manage Cinema Halls you can: create, retrieve, update, delete.
- Manage Genres you can: add, edit, delete.
- Manage Movies you can, add, edit, delete;
- Manage Actors you can add and manage actors' information;
- Schedule Movie Sessions: Set up movie sessions with show times, associated movies, and cinema halls;
- Book Tickets: Allow users to book tickets for specific movie sessions by selecting available seats;

### For this project you must use Docker.
Make sure that docker is working properly on your machine

### Installing using GitHub
Install PostgresSQL and create db

- git clone https://github.com/kostya-kononenko/Dockerize_DRF_Cinema.git
- cd cinema_API
- python -m venv venv
- source venv/bin/activate
- pip install -r requirements.txt

### Prepare docker-compose
To use docker-compose, create .env file and enter the following data there
  
- POSTGRES_HOST=db
- POSTGRES_USER=postgres
- POSTGRES_PASSWORD=secretpassword
- POSTGRES_DB=postgres
- POSTGRES_NAME=postgres

### Run server
- python manage.py migrate
- python manage.py runserver

### Run docker
- docker-compose build
- docker-compose up

### Getting access
- create user via /api/user/register/
- get access token via /api/user/token/
