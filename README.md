# Dockerizing DRF Cinema

- Read [the guideline](https://github.com/mate-academy/py-task-guideline/blob/main/README.md) before starting.
- Useful article on [Dockerizing Django with Postgres](https://saasitive.com/tutorial/django-celery-redis-postgres-docker-compose/) (without Celery & Redis, of course)

## Task

You need to fully dockerize this existing DRF project, Cinema.
Your service should be fully independent of your local machine.
The only requirement to run your project should be `Docker`.

### Task requirements

- Use `.dockerignore` to ignore unnecessary files in your images.
- Use a `Dockerfile` to build the `app` image with the DRF application.
- Use a `docker-compose.yml` file to manage multiple services (containers) at the same time.
- Switch to a `PostgreSQL` database instead of `SQLite` using the official Docker image.
- Implement a [`wait_for_db` management command](https://docs.djangoproject.com/en/4.2/howto/custom-management-commands/) that waits for the database to be available, so your services won't throw errors during `docker-compose up`.
- Make your Docker images as thin as possible.
- Use best practices for handling media, static files, and volumes with Docker.

### How to check that the task is done

1. Run `docker-compose up` and check with `docker ps` that 2 services are up and running (ensure that `app` always waits for `db` using the `wait_for_db` command).

1. Go to [127.0.0.1:8000/api/](http://127.0.0.1:8000/api/) and check project endpoints via the DRF interface (test image uploading as well).

1. Create a new admin user. Enter the container with:

```sh
docker exec -it <container_name> bash
```

and create the user from there.

1. Run tests using:

```sh
docker-compose run app sh -c "python manage.py test"
```

1. If needed, check flake8:

```sh
docker-compose run app sh -c "python manage.py test"
```

1. If everything is working fine, you are ready to push your code.
