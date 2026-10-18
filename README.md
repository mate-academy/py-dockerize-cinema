# Dockerizing DRF Cinema

- Read [the guideline](https://github.com/mate-academy/py-task-guideline/blob/main/README.md) before start
- Useful [link](https://saasitive.com/tutorial/django-celery-redis-postgres-docker-compose/) about theory 
  (without Celery & redis of course)

## Task:

Here, you need to fully dockerize this existing DRF project Cinema. 
You need to make your service fully independent of your local machine.
So the only requirement to run your project is `Docker`.

### Task requirements:
- Use `.dockerignore` for ignoring unnecessary stuff in your images;
- Use `Dockerfile` for building `app` image with DRF application;
- Use `docker-compose.yml` file for managing multiple services (containers) at the same time;
- Switch to `PostgreSQL` database instead of `SQLite` using official docker image;
- Implement `wait_for_db` 
  [management command](https://docs.djangoproject.com/en/4.2/howto/custom-management-commands/), 
  which waits for the database to be available. 
  So your services won't throw any errors during the `docker-compose up` command;
- Make your docker images as thin as possible;
- Use good practices of how to handle media, static files & volumes with docker.


### How to check, that task is done:
- Run `docker-compose up` command, and check with `docker ps`, that 2 services are up and running
  (here check, that `app` is always waiting for `db` using `wait_for_db` command);
- Go to `127.0.0.1:8000/api/cinema/` and check project endpoints via DRF interface (image uploading for sure);
- Create new admin user. Enter container `docker exec -it <container_name> bash`, and create in from there;
- Run tests using different approach: `docker-compose run app sh -c "python manage.py test"`;
- If needed, also check the flake8: `docker-compose run app sh -c "flake8"`.
- If everything is working fine - you are ready to push your code :).

## Run locally with Docker

Install Docker with the Compose plugin and start Docker Desktop. No local Python
or PostgreSQL installation is required. Run the following commands from the
project directory.

### 1. Configure the environment

In PowerShell, copy the example configuration:

```powershell
Copy-Item .env.example .env
```

On Linux or macOS, use `cp .env.example .env`. Edit `.env` and set your own
database password and Django secret key:

```dotenv
POSTGRES_DB=cinema
POSTGRES_USER=cinema
POSTGRES_PASSWORD=replace-with-your-local-database-password
POSTGRES_HOST=db
POSTGRES_PORT=5432
DJANGO_SECRET_KEY=replace-with-your-own-long-random-secret-key
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost
```

Keep `.env` private; commit only `.env.example` with placeholders. `db` is the
database service name inside the Compose network, so the application uses it
instead of `localhost` to connect to PostgreSQL.

### 2. Build and start the services

```sh
docker compose up --build -d
docker compose ps
docker compose logs app
```

Compose starts two services: `app` (Django on Python 3.10 slim, running as a
non-root user) and `db` (the official PostgreSQL 16 Alpine image). At startup,
the application runs `wait_for_db`, applies migrations, collects static files,
and starts Django at `0.0.0.0:8000` inside its container. The published address
on your computer is [http://127.0.0.1:8000/api/cinema/](http://127.0.0.1:8000/api/cinema/).

To follow startup messages, run `docker compose logs -f app`. Press `Ctrl+C`
to stop following the logs; the services continue running.

### 3. Create an administrator and check image uploads

```sh
docker compose exec app python manage.py createsuperuser
```

Enter an email address and password when prompted. Then check the browser flow:

1. Open [the API login page](http://127.0.0.1:8000/api-auth/login/) and sign in.
   Enter your email address in the field labelled **Username**.
2. Open [the movies endpoint](http://127.0.0.1:8000/api/cinema/movies/).
   Create a movie with `title`, `description`, and `duration` in minutes.
   Genres and actors can be left empty. Note the returned movie `id`.
3. Open `http://127.0.0.1:8000/api/cinema/movies/<id>/upload-image/`, replacing
   `<id>` with that number. Choose an image in the **Image** field and submit
   the **POST** form.
4. Open the returned `image` URL and confirm that the uploaded image is visible.

Session authentication supports the browser login. API clients can obtain JWT
access and refresh tokens by posting `email` and `password` to
[`/api/user/token/`](http://127.0.0.1:8000/api/user/token/), then send
`Authorization: Bearer <access-token>`. Interactive API documentation is at
[`/api/doc/swagger/`](http://127.0.0.1:8000/api/doc/swagger/).

### 4. Run tests and code style checks

```sh
docker compose run --rm app sh -c "python manage.py test && flake8"
```

This creates a temporary application container, runs Django tests followed by
Flake8 if the tests pass, and removes that container on exit. PostgreSQL must
be available; leave the services from step 2 running while executing checks.

### 5. Stop and restart without losing data

```sh
docker compose down
docker compose up -d
```

Named volumes retain PostgreSQL data (`postgres_data`), uploaded images
(`media_data`), and collected static files (`static_data`) when containers are
recreated. `docker compose down` preserves those volumes. Adding `-v` deletes
the project volumes and their data, so use it only when you intend to reset
the database and uploaded files.

### Development configuration

This setup uses Django's development server with `DJANGO_DEBUG=True`, serves
media for local checks, and publishes port 8000 on `127.0.0.1`. A production
deployment requires a separate configuration with a production application
server, `DEBUG=False`, appropriate hosts and secrets, and a web server or
storage service for static and media files.
