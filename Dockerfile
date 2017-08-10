# Run this exposing the directory of your choice as the /code volume:
# docker run -i --rm --volume "$(pwd)":/code flake8-codeclimate > codeclimate.json

FROM pypi/flake8
MAINTAINER cadams@loc.gov

RUN pip install --upgrade pip
# Until this is on PyPI we'll install from the GitHub repo instead:
# RUN pip install flake8-codeclimate
RUN pip install -e git+git://github.com/bennylope/flake8-codeclimate.git#egg=flake8_codeclimate

ENTRYPOINT flake8 --format=codeclimate /code
