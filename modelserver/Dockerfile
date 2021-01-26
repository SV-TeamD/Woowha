FROM python:3.7-slim-buster

WORKDIR /app

RUN  apt-get update \
  && apt-get install -y wget python3-venv libpq-dev \
  python3-pip python3-dev\
  && rm -rf /var/lib/apt/lists/*

ENV PYTHONUNBUFFERED=1

ENV DATABASE_URL=postgresql+psycopg2://user:1234@postgres_db:5432/app

RUN export PIP_CACHE_DIR=pip cache dir
COPY ./requirements.txt /app/requirements.txt
RUN --mount=type=cache,target=$PIP_CACHE_DIR pip3 install -r requirements.txt
