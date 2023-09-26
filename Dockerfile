FROM python:3.11.4-slim-buster

WORKDIR /app

COPY . /app

#COPY ./requirements.txt /app
RUN pip install -r requirements.txt
RUN python -m manage collectstatic
