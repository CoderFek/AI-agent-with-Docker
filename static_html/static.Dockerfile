# Declare the image to use

FROM python:3.13.5-slim-bullseye

WORKDIR /app

COPY ./src .

# RUN echo "hello" > index.html

