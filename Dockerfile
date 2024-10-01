FROM ubuntu:latest
LABEL authors="User"

ENTRYPOINT ["top", "-b"]