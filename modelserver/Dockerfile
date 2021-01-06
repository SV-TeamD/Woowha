FROM python:3.7-slim-buster

COPY requirements.txt /app/

RUN pip install -r /app/requirements.txt

# 모델 불러와서 캐싱해야 한다
# RUN python -c "from keras.applications import ResNet50; ResNet50(weights='imagenet')"

ENV PYTHONUNBUFFERED=0
COPY . /app

# CMD ["python", "/app/main.py"]
