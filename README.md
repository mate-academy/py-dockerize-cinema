# 🎬 Cinema Service API

## Overview
Cinema Service API is a Django REST Framework project for managing movies, cinema halls, sessions, and ticket bookings. It supports user registration, JWT authentication, and interactive API documentation.

## Getting Started
Clone the repo and run with Docker:
```bash
git clone https://github.com/your-username/py-dockerize-cinema.git
cd py-dockerize-cinema
docker-compose up --build
```

Create a superuser:
```bash
docker-compose run app python manage.py createsuperuser
```

## API Docs
Swagger UI → http://127.0.0.1:8000/api/docs/swagger-ui/

Redoc → http://127.0.0.1:8000/api/docs/redoc/

JSON Schema → http://127.0.0.1:8000/api/schema/

## Authentication
JWT endpoints:

- POST /api/user/token/ → obtain token

- POST /api/user/token/refresh/ → refresh token

- POST /api/user/token/verify/ → verify token

## Example Requests
Register a user:
```http
POST /api/user/register/
{
  "email": "user@example.com",
  "password": "strong_password",
  "first_name": "John",
  "last_name": "Doe"
}
```
## Running Tests

```bash
docker-compose run app sh -c "python manage.py test"
```
