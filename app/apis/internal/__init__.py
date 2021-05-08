"""
app.apis.internal.__init__.py
--------------------------

"""
from flask_restful import Api

from apis.internal import config


def init_app(api: Api):
    """
    :param api:
    :return:
    """
    # internal_api = Blueprint('internal_api', internal)
    # api = Api(internal_api)
    #
    # load_endpoints(api)
    # app.register_blueprint(api, url_prefix="/api")

    load_endpoints(api)

    # internal.init_app(app)


def load_endpoints(api: Api):
    """

    :param api:
    :return:
    """
    PREFIX = '/api'

    api.add_resource(config.Configuration, PREFIX + '/config')
    api.add_resource(config.SetupPage, PREFIX + '/setup_page')
