#!/bin/sh

echo "Wait db"
while ! nc -z $POSTGRES_DB $POSTGRES_PORT; do
  sleep 0.1
done

echo "Connected"