# Declare the image to use

FROM python:3.13.5-slim-bullseye

WORKDIR /app

COPY ./static_html .

# RUN echo "hello" > index.html

