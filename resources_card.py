from models_card import Card
from db import session

from flask_restful import reqparse
from flask_restful import abort
from flask_restful import Resource
from flask_restful import fields
from flask_restful import marshal_with

from models_link import Link
from resources_link import link_fields

card_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'content': fields.String,
    'uri': fields.Url('card', absolute=True),
    'links': fields.Nested(link_fields),
}


def links_parser(value):
    if not value or not 'url' in value:
        raise ValueError("Missing \'url\' in link.")
    return value


parser = reqparse.RequestParser()
parser.add_argument('title', type=str)
parser.add_argument('content', type=str)
parser.add_argument('links', type=links_parser, action='append')


class CardResource(Resource):
    @marshal_with(card_fields)
    def get(self, id):
        card = session.query(Card).filter(Card.id == id).first()
        if not card:
            abort(404, message="Card {} doesn't exist".format(id))
        return card

    def delete(self, id):
        card = session.query(Card).filter(Card.id == id).first()
        if not card:
            abort(404, message="Card {} doesn't exist".format(id))
        # TODO: delete card's links
        session.delete(card)
        session.commit()
        return {}, 204

    @marshal_with(card_fields)
    def put(self, id):
        parsed_args = parser.parse_args()
        card = session.query(Card).filter(Card.id == id).first()
        card.title = parsed_args['title']
        card.content = parsed_args['content']
        # TODO: use old links (now new ones are created)
        if 'links' in parsed_args and parsed_args['links'] is not None:
            for l in parsed_args['links']:
                print(l['url'])
                link = Link(url=l['url'])
                card.links.append(link)
        session.add(card)
        session.commit()
        return card, 201


class CardListResource(Resource):
    @marshal_with(card_fields)
    def get(self):
        cards = session.query(Card).all()
        return cards

    @marshal_with(card_fields)
    def post(self):
        parsed_args = parser.parse_args()
        card = Card(title=parsed_args['title'], content=parsed_args['content'])
        print(parsed_args)
        if 'links' in parsed_args and parsed_args['links'] is not None:
            for l in parsed_args['links']:
                print(l['url'])
                link = Link(url=l['url'])
                card.links.append(link)
        session.add(card)
        session.commit()
        return card, 201
