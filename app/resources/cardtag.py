from db import session

from flask_restful import reqparse
from flask_restful import abort
from flask_restful import Resource
from flask_restful import fields
from flask_restful import marshal_with

from models.card import Card
from models.tag import Tag, CardTag

cardtag_fields = {
    'card_id': fields.Integer,
    'tag_id': fields.Integer,
}

parser_cardtag = reqparse.RequestParser()
parser_cardtag.add_argument('tag_id', type=int)

parser_tagcard = reqparse.RequestParser()
parser_tagcard.add_argument('card_id', type=int)


def post_cardtag(card_id, tag_id):
    cardtag = CardTag(tag_id=tag_id, card_id=card_id)

    session.add(cardtag)
    session.commit()
    return cardtag, 201


def put_cardtag(card_id, tag_id):
    cardtag = session.query(CardTag).filter(CardTag.card_id == card_id).filter(CardTag.tag_id == tag_id).first()
    if not cardtag:
        return post_cardtag(card_id, tag_id)
    return cardtag, 200


class CardTagResource(Resource):
    @marshal_with(cardtag_fields)
    def get(self, card_id, tag_id):
        cardtags = session.query(CardTag).filter(CardTag.card_id == card_id).filter(CardTag.tag_id == tag_id).all()
        if not cardtags:
            abort(404, message="Relation {} doesn't exist".format(id))
        return cardtags

    def delete(self, card_id, tag_id):
        cardtags = session.query(CardTag).filter(CardTag.card_id == card_id).filter(CardTag.tag_id == tag_id).all()
        if not cardtags:
            abort(404, message="Relation {} doesn't exist".format(id))
        session.delete(cardtags)
        session.commit()
        return {}, 204

    @marshal_with(cardtag_fields)
    def put(self, card_id, tag_id):
        card = session.query(Card).filter(Card.id == card_id).first()
        if not card:
            abort(404, message="Card {} doesn't exist".format(card_id))
        return put_cardtag(card_id=card_id, tag_id=tag_id)

    @marshal_with(cardtag_fields)
    def post(self, card_id, tag_id):
        card = session.query(Card).filter(Card.id == card_id).first()
        if not card:
            abort(404, message="Card {} doesn't exist".format(card_id))
        return post_cardtag(card_id=card_id, tag_id=tag_id)


class CardTagListResource(Resource):
    @marshal_with(cardtag_fields)
    def get(self, card_id):
        cardtags = session.query(CardTag).filter(CardTag.card_id == card_id).all()
        return cardtags

    @marshal_with(cardtag_fields)
    def post(self, card_id):
        card = session.query(Card).filter(Card.id == card_id).first()
        if not card:
            abort(404, message="Card {} doesn't exist".format(card_id))
        parsed_args = parser_cardtag.parse_args()
        return post_cardtag(card_id=card.id, tag_id=parsed_args['tag_id'])


class TagCardListResource(Resource):
    @marshal_with(cardtag_fields)
    def get(self, tag_id):
        cardtags = session.query(CardTag).filter(CardTag.tag_id == tag_id).all()
        return cardtags

    @marshal_with(cardtag_fields)
    def post(self, tag_id):
        tag = session.query(Tag).filter(Tag.id == tag_id).first()
        if not tag:
            abort(404, message="Tag {} doesn't exist".format(tag_id))
        parsed_args = parser_tagcard.parse_args()
        return post_cardtag(card_id=parsed_args['card_id'], tag_id=tag.id)


class TagCardResource(Resource):
    @marshal_with(cardtag_fields)
    def get(self, card_id, tag_id):
        cardtags = session.query(CardTag).filter(CardTag.card_id == card_id).filter(CardTag.tag_id == tag_id).all()
        if not cardtags:
            abort(404, message="Relation {} doesn't exist".format(id))
        return cardtags

    def delete(self, card_id, tag_id):
        cardtags = session.query(CardTag).filter(CardTag.card_id == card_id).filter(CardTag.tag_id == tag_id).all()
        if not cardtags:
            abort(404, message="Relation {} doesn't exist".format(id))
        session.delete(cardtags)
        session.commit()
        return {}, 204

    @marshal_with(cardtag_fields)
    def put(self, card_id, tag_id):
        tag = session.query(Tag).filter(Tag.id == tag_id).first()
        if not tag:
            abort(404, message="Tag {} doesn't exist".format(tag_id))
        return put_cardtag(card_id=card_id, tag_id=tag.id)

    @marshal_with(cardtag_fields)
    def post(self, card_id, tag_id):
        tag = session.query(Tag).filter(Tag.id == tag_id).first()
        if not tag:
            abort(404, message="Tag {} doesn't exist".format(tag_id))
        return post_cardtag(card_id=card_id, tag_id=tag.id)
