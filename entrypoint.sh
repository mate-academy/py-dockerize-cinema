#!/bin/sh
set -e

mkdir -p /files/media/uploads/movies
chown -R my_user:my_user /files/media
chmod -R 775 /files/media

exec su-exec my_user "$@"