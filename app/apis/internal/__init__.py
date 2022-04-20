"""
app.apis.internal.__init__.py
--------------------------

"""
from flask_restful import Api
from apis.internal import config


def evaluate_url(url, prefix_url):
    """

    :param url:
    :param prefix_url:
    :return:
    """
    return (prefix_url if prefix_url else '') + url

def init_app(api: Api, prefix_url=None):
    """
    :param api:
    :return:
    """
    # internal_api = Blueprint('internal_api', internal)
    # api = Api(internal_api)
    #
    # load_endpoints(api)
    # app.register_blueprint(api, url_prefix="/api")

    load_endpoints(api, prefix_url)

    # internal.init_app(app)


def load_endpoints(api: Api, prefix_url):
    """
    :param api:
    :return:
    """
    api.add_resource(config.Configuration, evaluate_url('/configuration/<string:tool_config_id>/', prefix_url))
    api.add_resource(config.Configurations, evaluate_url('/configurations/', prefix_url))