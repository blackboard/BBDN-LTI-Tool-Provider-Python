"""
api/__init__.py
-------------------------------------------------------------------
"""
from routes.api import internal
from routes.api import api


def init_app(app):
    """
    :param app:
    :return:
    """
    app.register_blueprint(api, url_prefix="/api")
    internal.init_app(app)