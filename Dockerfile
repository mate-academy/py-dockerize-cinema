FROM ubuntu:latest
LABEL authors="zazul"

ENTRYPOINT ["top", "-b"]