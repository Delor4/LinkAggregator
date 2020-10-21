#!/usr/bin/env python
import os

from flask import Flask, send_file
from flask_restful import Api
from flask_cors import CORS

from classes.config import config

app = Flask(__name__)
app.config.from_object(config)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
api = Api(app)

from resources.card import CardListResource, CardResource
from resources.link import LinkListResource, LinkResource
from resources.tag import TagListResource, TagResource
from resources.cardtag import CardTagResource, CardTagListResource
from resources.cardtag import TagCardResource, TagCardListResource

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


# Everything not declared before (not a Flask route / API endpoint)...
@app.route("/<path:path>")
def route_frontend(path):
    # ...could be a static file needed by the front end that
    # doesn't use the `static` path (like in `<script src="bundle.js">`)
    file_path = os.path.join(app.static_folder, path)
    if os.path.isfile(file_path):
        return send_file(file_path)
    # ...or should be handled by the SPA's "router" in front end
    else:
        index_path = os.path.join(app.static_folder, "index.html")
        return send_file(index_path)


if __name__ == '__main__':
    app.run(port=44343, debug=True)
