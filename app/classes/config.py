import os

from flask import Config

config = Config('./')
config.from_pyfile(os.environ.get("LINKAGGREGATOR_CONFIG", 'settings.py'))
