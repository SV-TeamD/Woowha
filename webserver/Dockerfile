FROM ubuntu:20.04

WORKDIR /app

RUN apt-get update -y && \
  apt-get install -y python3-pip python3-dev \
  build-essential libssl-dev libffi-dev python3-setuptools \
  python3-venv libpq-dev

ENV FLASK_APP=app.py
ENV PYTHONUNBUFFERED=1

ENV DATABASE_URL=postgresql+psycopg2://user:1234@postgres_db:5432/app
ENV WAIT_FOR_OUTPUT_IMAGE_SECOND=30

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
