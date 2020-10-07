
BIN=../venv/bin/

.PHONY: all install run init_db

all:

install:
	$(BIN)pip install -r requirements.txt

run:
	$(BIN)python app.py


init_db:
	$(BIN)python manage.py db init
