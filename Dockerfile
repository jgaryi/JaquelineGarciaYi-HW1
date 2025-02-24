## Start with a base image, such as 3.11-slim-buster
FROM python:3.11-slim-buster

## Ensure we have an up to date baseline and install any OS dependencies
## Add a user app like we did in tutorials
## Use RUN commands to install necessary packages
RUN set -ex; \
    apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends build-essential git ffmpeg && \
    pip install --no-cache-dir --upgrade pip && \
    pip install pipenv && \
    mkdir -p /app

## Set the working directory to /app
WORKDIR /app

## Add Pipfile, Pipfile.lock
ADD Pipfile Pipfile.lock /app/

## Ensure you are running pipenv sync
RUN pipenv sync

## Source code
ADD . /app

## Set your entry point to /bin/bash
ENTRYPOINT ["/bin/bash"]

## Set your command to open up pipenv shell
CMD ["-c", "pipenv shell"]