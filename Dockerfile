FROM --platform=linux/amd64 python:3.11.2-slim
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN mkdir /weather
WORKDIR /weather
COPY ./requirements.txt /weather
RUN apt update && \
    apt upgrade -y && \
    apt install make -y && \
    python -m pip install --upgrade pip
RUN pip install -r requirements.txt
COPY weather/bot_weather_forecast /weather
