"""
app.apis.ims.jwks
-----------------

"""

import logging

import logs
from flask import current_app, request
from flask_restful import Resource


class WellKnownJWKS(Resource):
    """

    """

    def get(self):
        """

        :return:
        """

        logs.api_logger.log(logging.INFO, "Request /jwks",
                            extra={'clientip': request.remote_addr, 'user': request.remote_user})

        return current_app.config['LTI_TOOL_CONFIG'].get_jwks()
