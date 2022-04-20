import logging

import logs

from flask import Blueprint
from flask_restful import Api

from apis import internal, ims


def init_app(app):
    """
    :param app:
    :return:
    """

    api_blueprint = Blueprint('api', __name__)

    api = Api(api_blueprint)

    logs.server_logger.info('Initializing API')

    internal.init_app(api, '/internal')
    ims.init_app(api, '/ims')

    app.register_blueprint(api_blueprint)

    # api = Api(app)
    # internal.init_app(api)
    # ims.init_app(api)
