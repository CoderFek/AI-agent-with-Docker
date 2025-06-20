# Declare the image to use

FROM python:3.13.5-slim-bullseye

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

RUN pip install -r /tmp/requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]