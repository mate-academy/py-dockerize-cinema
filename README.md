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
- Go to `127.0.0.1:8000/api/` and check project endpoints via DRF interface (image uploading for sure);
- Create new admin user. Enter container `docker exec -it <container_name> bash`, and create in from there;
- Run tests using different approach: `docker-compose run app sh -c "python manage.py test"`;
- If needed, also check the flake8: `docker-compose run app sh -c "flake8"`.
- If everything is working fine - you are ready to push your code :).

## Run with Docker

Install Docker with the Compose plugin. No local Python or PostgreSQL install
is required. From the repository directory:

```sh
cp .env.example .env
# Edit .env and replace SECRET_KEY and POSTGRES_PASSWORD.
docker compose up --build
```

Open http://127.0.0.1:8000/api/ for the browsable API or
http://127.0.0.1:8000/api/doc/swagger/ for interactive documentation.
The app waits for a healthy PostgreSQL service, runs `wait_for_db`, applies
migrations, collects static assets, then starts Django on port 8000.
`wait_for_db` retries real database queries for up to 60 seconds and exits
with a clear error if the database never becomes available.

This is a local development setup: `DEBUG=1` enables Django's static and
uploaded-media serving. For production, use a production application server
and a dedicated static/media server or storage service with `DEBUG=0`.
The app runs as an unprivileged user; PostgreSQL is accessible only inside
the Compose network. Database, media, and collected static files use separate
named volumes and survive container replacement. Source code is built into
the image; rebuild after changing it.

## Admin and image uploads

In a second terminal:

```sh
docker compose exec app python manage.py createsuperuser
```

Enter an email and password, then sign in at http://127.0.0.1:8000/admin/.
Create a movie and upload its image there, or use the Swagger interface:
obtain a token from `/api/user/token/`, use **Authorize** with the access
token, create a movie, then call
`POST /api/cinema/movies/{id}/upload-image/` with an image file.
The API requires an administrator for image uploads. Uploaded images are
served from `/media/uploads/movies/` and stored in the media volume.

## Tests and checks

```sh
docker compose run --rm app python manage.py test
docker compose run --rm app python manage.py check
docker compose run --rm app python manage.py makemigrations --check --dry-run
```

The default image omits development linting tools. To run the assignment's
flake8 command, build with those tools enabled:

```sh
INSTALL_DEV=true docker compose build app
docker compose run --rm app flake8
docker compose run --rm app pip check
```

CI runs the full suite against PostgreSQL, checks migrations and style,
then exercises JWT login, movie creation, image upload, media download,
and static CSS over HTTP. It recreates both containers without deleting
volumes and verifies the movie and image are still available.

## Stop and restart

```sh
docker compose down
docker compose up -d
```

These commands preserve data. `docker compose down --volumes` permanently
removes this project's database and uploaded files; use it only to reset
disposable data. Changing the database password in `.env` does not update
an already initialized PostgreSQL volume.
