FROM python:3.7-slim-buster

ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY . /app

# 모델 불러와서 캐싱해야 한다
# RUN python -c "from keras.applications import ResNet50; ResNet50(weights='imagenet')"

