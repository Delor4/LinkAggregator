#!/usr/bin/env python

from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

from resources_card import CardListResource, CardResource
from resources_link import LinkListResource, LinkResource

api.add_resource(CardListResource, '/api/cards', endpoint='cards')
api.add_resource(CardResource, '/api/cards/<string:id>', endpoint='card')

api.add_resource(LinkListResource, '/api/links', endpoint='links')
api.add_resource(LinkResource, '/api/links/<string:id>', endpoint='link')

if __name__ == '__main__':
    app.run(port=44343, debug=True)
