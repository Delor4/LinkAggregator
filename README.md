[Link Aggregator](https://github.com/Delor4/LinkAggregator)
===================

RESTful HTTP API using [Flask](https://github.com/pallets/flask), [Flask-Restful](https://github.com/flask-restful/flask-restful) and [SQLAlchemy](https://github.com/zzzeek/sqlalchemy)
-------------------

1. Install requisite packages:
```shell
$ pip install -r api/requirements.txt
```
2. Create tables:
```shell
$ ./api/create_db.py
```
3. Run service:
```
$ python api/app.py
```
4. List of endpoints:

- `/api/cards`
(Methods: `GET` `POST` `GET /<id>` `PUT /<id>` `DELETE /<id>`)
- `/api/links`
(Methods: `GET` `POST` `GET /<id>` `PUT /<id>` `DELETE /<id>`)
- `/api/tags`
(Methods: `GET` `POST` `GET /<id>` `PUT /<id>` `DELETE /<id>`)
- `/api/cards/<card_id>/tags`
(Methods: `GET` `POST` `GET /<id>` `POST /<id>` `PUT /<id>` `DELETE /<id>`) 
- `/api/tags/<tag_id>/cards`
(Methods: `GET` `POST` `GET /<id>` `POST /<id>` `PUT /<id>` `DELETE /<id>`) 

Don't forget add "Content-Type: application/json" header to your request!
