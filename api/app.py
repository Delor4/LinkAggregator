#!/usr/bin/env python

from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

from api.resources.card import CardListResource, CardResource
from api.resources.link import LinkListResource, LinkResource
from api.resources.tag import TagListResource, TagResource
from api.resources.cardtag import CardTagResource, CardTagListResource
from api.resources.cardtag import TagCardResource, TagCardListResource

api.add_resource(CardListResource, '/api/cards', endpoint='cards')
api.add_resource(CardResource, '/api/cards/<string:id>', endpoint='card')

api.add_resource(LinkListResource, '/api/links', endpoint='links')
api.add_resource(LinkResource, '/api/links/<string:id>', endpoint='link')

api.add_resource(TagListResource, '/api/tags', endpoint='tags')
api.add_resource(TagResource, '/api/tags/<string:id>', endpoint='tag')

api.add_resource(CardTagListResource, '/api/cards/<string:card_id>/tags', endpoint='cardtags')
api.add_resource(CardTagResource, '/api/cards/<string:card_id>/tags/<string:tag_id>', endpoint='cardtag')

api.add_resource(TagCardListResource, '/api/tags/<string:tag_id>/cards', endpoint='tagcards')
api.add_resource(TagCardResource, '/api/tags/<string:tag_id>/cards/<string:card_id>', endpoint='tagcard')

@app.after_request
def add_header(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Access-Control-Allow-Headers, Origin, X-Requested-With, Content-Type, Accept, Authorization'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS, HEAD, PATCH'
    response.headers['Access-Control-Expose-Headers'] = '*'
    return response

if __name__ == '__main__':
    app.run(port=44343, debug=True)
