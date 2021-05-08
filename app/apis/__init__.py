import logging

from flask import Blueprint
from flask_restful import Api

from apis import internal, ims
from logging import Logger

def init_app(app):
    """
    :param app:
    :return:
    """

    logger = logging.getLogger('info')
    logger.log(logging.INFO, 'Initializing API')

    api_blueprint = Blueprint('api', __name__)

    api = Api(api_blueprint)

    internal.init_app(api)
    ims.init_app(api)

    app.register_blueprint(api_blueprint)

    # api = Api(app)
    # internal.init_app(api)
    # ims.init_app(api)
