

### Task requirements:

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
