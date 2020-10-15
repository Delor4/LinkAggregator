
BIN=../venv/bin/

.PHONY: all install run init_db

all:

install:
	pip install -r requirements.txt

run:
	python app.py


init_db:
	python manage.py db init
