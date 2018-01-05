Flask Docker Gunicorn Sample
============================

Sample Docker setup using Flask, Gunicorn, and Nginx.

# Setup

You'll need to install Docker and Docker Compose if you haven't.


- Install Docker and Docker Compose for Mac: https://docs.docker.com/docker-for-mac/install/


- Install Docker: https://docs.docker.com/engine/installation/
- Install Docker Compose: https://docs.docker.com/compose/install/

#### Build

    $ docker-compose build

#### Run

With the flask server:

    $ docker-compose -f docker-compose.local.yml up -d --force-recreate

With nginx and gunicorn:

    $ docker-compose up -d --force-recreate

