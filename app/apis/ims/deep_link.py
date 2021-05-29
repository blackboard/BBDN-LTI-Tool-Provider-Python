"""
app.apis.ims.deep_link
----------------------
Deeplinking methods
"""

import json

from flask import request, redirect, current_app
from flask_restful import Resource

import logs
from cache import cache
from helpers.dynamic_content import generate_token
from ims.deep_link import deep_link_content, deep_link_frame
# Constants
# DEEPLINK_BODY = 'https://purl.imsglobal.org/spec/lti-dl/claim/deep_linking_settings'
# DEPLOYMENT_ID = 'https://purl.imsglobal.org/spec/lti/claim/deployment_id'
from ims.jwt_management import decode_jwt


class DeepLinkingPayloadData(Resource):
    """
    Deeplink payload
    """

    def get(self):
        """
        Get method to obtain the payload from the token
        :param token
        :return:
        """
        token = request.values['token']
        logs.api_logger.info("DeepLinking Payload Data: " + str(token),
                             extra={"clientip": request.remote_addr, 'path': request.path, "user": request.remote_user})
        payload = cache.get(token)

        return payload


class DeepLinkingContent(Resource):
    """
    Deep Linking Content
    """

    def post(self):
        """
        Post method to obtain the Deeplink content payload
        :return:
        """

        # parser = reqparse.RequestParser()
        logs.api_logger.info("DeepLinking Content: " + str(request.data),
                             extra={"clientip": request.remote_addr, 'path': request.path, "user": request.remote_user})

        request_json = json.loads(request.data)

        lti_content = request_json["deep_link_content"]

        content = deep_link_content(lti_content)

        return content


class DeepLinkingOptions(Resource):
    """
    Deeplink Option
    """

    def post(self):
        """
        Post method
        :return:
        """

        jwt_token = request.values['id_token']

        jwt_payload = decode_jwt(jwt_token, "https://blackboard.com")

        token = generate_token(jwt_payload)
        cache.set(token, jwt_payload)

        redirection = redirect('http://localhost:3000/deepLinkContent/' + token)

        return redirection


class DeepLinkingFrame(Resource):
    """

    """

    def post(self):
        """

        :return:
        """
        request_json = json.loads(request.data)
        content = request_json['items']
        deploy = request_json['payload']['https://purl.imsglobal.org/spec/lti/claim/deployment_id']
        deepLink = request_json['payload']["https://purl.imsglobal.org/spec/lti-dl/claim/deep_linking_settings"];
        data = deepLink['data']
        iss = request.data['payload']['iss']
        frame = deep_link_frame(current_app.settings['LTI_TOOL_CONFIG'].get_client_id(), iss, deploy, data, content)

        return frame
