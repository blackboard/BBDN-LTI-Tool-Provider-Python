"""
app.apis.ims.deep_link
----------------------

"""
import json

import logging

import logs
from logging import Logger
from config import Settings, settings

from flask import Response, request, redirect, current_app
from flask_restful import Resource, fields, marshal_with, reqparse

from ims.deep_link import deep_link_content, deep_link_frame


# Constants
# DEEPLINK_BODY = 'https://purl.imsglobal.org/spec/lti-dl/claim/deep_linking_settings'
# DEPLOYMENT_ID = 'https://purl.imsglobal.org/spec/lti/claim/deployment_id'


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

        # parser = reqparse.RequestParser()
        logs.api_logger.info("DeepLinking Content: " + str(request.data))

        lti_content = json.loads(request.data)["deep_link_content"]

        content = deep_link_content(lti_content)

        return content


class DeepLinkingOptions(Resource):
    """

    """

    def get(self):
        """

        :return:
        """
        return redirect('http://localhost:3000/ltiContent')

    def post(self):
        """

        :return:
        """
        return redirect('http://localhost:3000/ltiContent')


class DeepLinkingFrame(Resource):
    """

    """

    def post(self):
        """

        :return:
        """
        deploy = request.data['payload']['https://purl.imsglobal.org/spec/lti/claim/deployment_id']
        items = request.data['items']
        deepLink = request.data['payload']["https://purl.imsglobal.org/spec/lti-dl/claim/deep_linking_settings"];
        data = deepLink['data']
        iss = request.data['payload']['iss']
        deep_link_frame(current_app.settings['LTI_TOOL_CONFIG'].get_client_id(), iss, deploy, data, items)
