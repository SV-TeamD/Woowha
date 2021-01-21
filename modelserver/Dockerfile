FROM python:3.7-slim-buster

RUN  apt-get update \
  && apt-get install -y wget python3-venv libpq-dev \
  python3-pip python3-dev\
  && rm -rf /var/lib/apt/lists/*

ENV PYTHONUNBUFFERED=1
ENV DATABASE_URL=postgresql+psycopg2://user:1234@postgres_db:5432/app

WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY . /app
