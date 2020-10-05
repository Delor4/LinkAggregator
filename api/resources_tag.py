from api.db import session

from flask_restful import reqparse
from flask_restful import abort
from flask_restful import Resource
from flask_restful import fields
from flask_restful import marshal_with

from api.models.tag import Tag

tag_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'uri': fields.Url('tag', absolute=True),
}

parser = reqparse.RequestParser()
parser.add_argument('name', type=str)


class TagResource(Resource):
    @marshal_with(tag_fields)
    def get(self, id):
        tag = session.query(Tag).filter(Tag.id == id).first()
        if not tag:
            abort(404, message="Tag {} doesn't exist".format(id))
        return tag

    def delete(self, id):
        tag = session.query(Tag).filter(Tag.id == id).first()
        if not tag:
            abort(404, message="Tag {} doesn't exist".format(id))
        # TODO: delete tags's cardtag records
        session.delete(tag)
        session.commit()
        return {}, 204

    @marshal_with(tag_fields)
    def put(self, id):
        parsed_args = parser.parse_args()
        tag = session.query(Tag).filter(Tag.id == id).first()
        tag.name = parsed_args['name']
        session.add(tag)
        session.commit()
        return tag, 201


class TagListResource(Resource):
    @marshal_with(tag_fields)
    def get(self):
        tags = session.query(Tag).all()
        return tags

    @marshal_with(tag_fields)
    def post(self):
        parsed_args = parser.parse_args()
        tag = Tag(name=parsed_args['name'])
        session.add(tag)
        session.commit()
        return tag, 201
