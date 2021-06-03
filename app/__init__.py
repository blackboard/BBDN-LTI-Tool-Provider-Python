"""
app.__init__
------------
Application factory
"""

import apis
import os

from flask import Flask
from flask_cors import CORS

from cache import cache
from config import settings


def init_app() -> Flask:
    """
    :return:
    """

    app = Flask(__name__)
    cors = CORS(app, resources={"*": {"origins": "*"}})
    apis.init_app(app)
    # logging.basicConfig(filename='logs/server.log', level=logging.INFO)

    return app


def create_app(config=None):
    """
    :param config:
    :return:
    """
    app = init_app()

    # load default configuration
    app.config.from_object(settings)
    # load environment configuration
    if 'FLASK_CONF' in os.environ:
        app.config.from_envvar('FLASK_CONF')
    # load app specified configuration
    if config is not None:
        if isinstance(config, dict):
            app.config.update(config)
        elif config.endswith('.py'):
            app.config.from_pyfile(config)
    cache.init_app(app)
    return app

