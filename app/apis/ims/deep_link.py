"""
app.apis.ims.deep_link
----------------------

"""
import json
import logging
from logging import Logger

from flask import Response, request
from flask_restful import Resource, fields, marshal_with, reqparse

from ims.deep_link import deep_link_content

# Constants
DEEPLINK_BODY = 'https://purl.imsglobal.org/spec/lti-dl/claim/deep_linking_settings'
DEPLOYMENT_ID = 'https://purl.imsglobal.org/spec/lti/claim/deployment_id'


class DeepLinkingPayloadData(Resource):
    """

    """

    def get(self):
        """

        :return:
        """
        pass


class DeepLinkingContent(Resource):
    """

    """

    def post(self):
        """

        :return:
        """

        parser = reqparse.RequestParser()
        # Logger.log(logging.INFO, "Deeplink Content")

        lti_content = json.loads(request.data)["deep_link_content"]

        content = deep_link_content(lti_content)

        return content
