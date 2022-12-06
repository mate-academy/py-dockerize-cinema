# Cinema API

API service for cinema management written on DRF 

## Installing using GitHub

Install PostgreSQL and create db
```
git clone https://github.com/Nikyxa/cinema-api.git
python3 -m venv venv
source venv/bin/activate (Linux and macOS) or venv\Scripts\activate (Windows)
pip install -r requirements.txt
set DB_HOST=<your db hostname>
set DB_NAME=<your db name>
set DB_USER=<your db username>
set DB_PASSWORD=<your db user password>
python manage.py migrate
python manage.py runserver
```

## Run with Docker
Docker should be installed

```
docker-compose build
docker-compose up
```


## Getting access

- create user via /api/user/register/
- get access token via /api/user/token/

## Features
- JWT authenticated 
- Admin panel /admin/ 
- Documentation is located at /api/doc/swagger/ 
- Managing orders and tickets 
- Creating movies with genres, actors and image 
- Creating cinema halls 
- Adding movie sessions 
- Filtering movies and movie sessions