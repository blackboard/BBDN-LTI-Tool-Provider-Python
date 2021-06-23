"""
app.apis.ims.jwks
-----------------

"""

import logging

import logs
from flask import current_app, request
from flask_restful import Resource


class HealthCheck(Resource):
    """

    """

    def get(self):
        """

        :return:
        """

        logs.api_logger.log(logging.INFO, "Request /healthCheck",
                            extra={'clientip': request.remote_addr, 'user': request.remote_user})

        return 200
