
DOCKER_DIR = docker
BACK_DIR = app
FRONT_DIR = link-aggregator

.PHONY: all install run

all:

install:
	pip install -r requirements.txt

run:
	python app.py

init_db:
	python manage.py db init
