from db import session

from flask_restful import reqparse
from flask_restful import abort
from flask_restful import Resource
from flask_restful import fields
from flask_restful import marshal_with

from models.card import Card
from models.link import Link

link_fields = {
    'id': fields.Integer,
    'url': fields.String,
    'uri': fields.Url('link', absolute=True),
    'card_id': fields.Integer,
}

parser = reqparse.RequestParser()
parser.add_argument('url', type=str)
parser.add_argument('card_id', type=int)


class LinkResource(Resource):
    @marshal_with(link_fields)
    def get(self, id):
        link = session.query(Link).filter(Link.id == id).first()
        if not link:
            abort(404, message="Link {} doesn't exist".format(id))
        return link

    def delete(self, id):
        link = session.query(Link).filter(Link.id == id).first()
        if not link:
            abort(404, message="Link {} doesn't exist".format(id))
        session.delete(link)
        session.commit()
        return {}, 204

    @marshal_with(link_fields)
    def put(self, id):
        parsed_args = parser.parse_args()
        link = session.query(Link).filter(Link.id == id).first()
        link.url = parsed_args['url']
        card = session.query(Card).filter(Card.id == parsed_args['card_id']).first()
        card.links.append(link)
        session.add(link)
        session.commit()
        return link, 201


class LinkListResource(Resource):
    @marshal_with(link_fields)
    def get(self):
        links = session.query(Link).all()
        return links

    @marshal_with(link_fields)
    def post(self):
        parsed_args = parser.parse_args()
        link = Link(url=parsed_args['url'])
        card = session.query(Card).filter(Card.id == parsed_args['card_id']).first()
        card.links.append(link)
        session.add(link)
        session.commit()
        return link, 201
