[Link Aggregator](https://github.com/Delor4/LinkAggregator)
===================
Place for your links.


RESTful HTTP API using [Flask](https://github.com/pallets/flask), [Flask-Restful](https://github.com/flask-restful/flask-restful) and [SQLAlchemy](https://github.com/zzzeek/sqlalchemy)
-------------------

```
cd app
```

- Install requisite packages:
```shell
$ pip install -r api/requirements.txt
```

- Create tables:
```shell
$ python app/create_db.py
```

- Run service:
```shell
$ python app/app.py
```
- List of endpoints:
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

Don't forget add `Content-Type: application/json` header to your request!

Frontend using [Vue.js](https://vuejs.org/) and [Bootstrap](https://bootstrap-vue.org/)
---

```
cd link-aggregator
```
- Run site:
```
npm run serve
```


Conteners by [Docker](https://www.docker.com/)
-----

- Make and run docker image
```shell
make all
