# Dockerizing DRF Cinema

- Read [the guideline](https://github.com/mate-academy/py-task-guideline/blob/main/README.md) before start
- Useful [link](https://soshace.com/dockerizing-django-with-postgres-redis-and-celery/) about theory 
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
  [management command](https://docs.djangoproject.com/en/4.0/howto/custom-management-commands/), 
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
