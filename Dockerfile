FROM python:3.7.2-slim

RUN mkdir /app
RUN apt-get update
RUN apt-get install -y libpq-dev
WORKDIR /app

COPY . .

RUN pip install Django psycopg2
