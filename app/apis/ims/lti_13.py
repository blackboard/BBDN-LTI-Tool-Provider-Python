"""
app.apis.ims.lti_13
-------------------
"""
import logging

from flask_restful import Resource
from pylti1p3.contrib.flask import FlaskCacheDataStorage, FlaskRequest, FlaskOIDCLogin

from cache import cache
from config import settings
from logs import api_logger


class Lti13Launch(Resource):
    """

    """

    def post(self):
        """

        :return:
        """
        api_logger.info("Lti 1.3 Launch")


class JWTPayloadData(Resource):
    """

    """

    def get(self):
        """

        :return:
        """
        pass


class Login(Resource):
    """

    """

    def get(self):
        """

        :return:
        """
        tool_conf = settings.LTI_TOOL_CONFIG
        launch_data_storage = FlaskCacheDataStorage(cache)

        request = FlaskRequest()
        target_link_uri = request.get_param('target_link_uri')

        if not target_link_uri:
            raise Exception('Missing "target_link_uri" param')

        oidc_login = FlaskOIDCLogin(request, tool_conf, launch_data_storage=launch_data_storage)
        return oidc_login.enable_check_cookies().redirect(target_link_uri)
