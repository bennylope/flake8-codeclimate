GIT_VERSION := $(shell python setup.py --version)

all: docker

docker:
	docker build -t flake8-codeclimate:latest .
	@if [[ "${GIT_VERSION}" != *"+"* ]]; then \
		docker tag flake8-codeclimate:latest flake8-codeclimate:${GIT_VERSION}; \
	fi
