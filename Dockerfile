# Run this exposing the directory of your choice as the /code volume:
# docker run -i --rm --volume "$(pwd)":/code flake8-codeclimate > codeclimate.json

FROM python:slim
LABEL maintainer="cadams@loc.gov"

RUN pip install --upgrade pip
RUN pip install flake8-codeclimate

ENTRYPOINT flake8 --format=codeclimate /code
