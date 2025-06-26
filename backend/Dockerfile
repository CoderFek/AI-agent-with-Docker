# Declare the image to use

FROM python:3.13.5-slim-bullseye

# host.docker.internal -> localhost
# curl -X POST -d '{"message": "Hello world"}'  -H "Content-Type: application/json" http://host.docker.internal:8080/api/chats/
RUN apt-get update && apt-get install -y curl

# Create python virtual environment
# add python virtual environment to path

RUN python -m venv /opt/venv
ENV PATH=/opt/venv/bin:$PATH

WORKDIR /app

COPY ./requirements.txt /tmp/requirements.txt

# RUN within_container_while_building
RUN pip install -r /tmp/requirements.txt

# COPY local_file conatiner_destination
COPY ./src .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]