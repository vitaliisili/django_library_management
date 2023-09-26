FROM python:3.11.4-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /app

# lint
RUN pip install --upgrade pip

COPY ./requirements.txt .
RUN pip install -r requirements.txt

RUN python -m manage collectstatic

COPY . .

RUN python -m manage makemigrations
RUN python -m manage migrate
