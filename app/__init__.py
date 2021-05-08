"""
app.__init__
------------
Application factory
"""
import logging
import os

from flask import Flask
from flask_cors import CORS

import apis


def init_app() -> Flask:
    """
    :return:
    """

    app = Flask(__name__)
    cors = CORS(app, resources={"*": {"origins": "*"}})
    logging.getLogger('info')
    logging.basicConfig(filename='server.log', level=logging.INFO)
    apis.init_app(app)

    return app


def create_app(config=None):
    """
    :param config:
    :return:
    """
    app = init_app()
    # load default configuration
    app.config.from_object('config.settings')
    # load environment configuration
    if 'FLASK_CONF' in os.environ:
        app.config.from_envvar('FLASK_CONF')
    # load app specified configuration
    if config is not None:
        if isinstance(config, dict):
            app.config.update(config)
        elif config.endswith('.py'):
            app.config.from_pyfile(config)
    return app
