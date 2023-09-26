FROM python:3.11.4-slim-buster

# base image
FROM python:3.8
# setup environment variable
ENV DockerHOME=/home/app/

# set work directory
RUN mkdir -p $DockerHOME

# where your code lives
WORKDIR $DockerHOME

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip

# copy whole project to your docker home directory.
COPY . $DockerHOME
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . $DockerHOME
RUN python -m manage collectstatic
COPY . $DockerHOME

RUN python -m manage makemigrations
RUN python -m manage migrate
