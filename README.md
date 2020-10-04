Demo RESTful HTTP API using [Flask](https://github.com/pallets/flask), [Flask-Restful](https://github.com/flask-restful/flask-restful) and [SQLAlchemy](https://github.com/zzzeek/sqlalchemy)
===================

1. Install requisite packages:
```shell
$ pip install -r requirements.txt
```
2. Create tables:
```shell
$ ./create_db.py
```
3. Run service:
```
$ python app.py
```
4. List of endpoints:

- `/api/cards` 
- `/api/links`

Allowed methods:
- GET
- POST
- GET /<id>
- PUT /<id>
- DELETE /<id>

Don't forget that you must pass a "Content-Type: application/json" header along with your request!
