FROM python:3.7.9-slim

ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update && \
    apt-get install build-essential -y && \
    apt-get install libpq-dev -y && \
    apt-get install gcc -y

RUN mkdir /flask_app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

#ADD . /flask_app

WORKDIR /flask_app