"""
app.apis.ims.deep_link
----------------------
Deeplinking methods
"""

import json
import pprint
import time
import uuid
import jwt  # type: ignore
import sys

from flask import request, redirect, current_app
from flask_restful import Resource

import logs
from cache import cache
from helpers.aws_connection import get_files_from_bucket
from helpers.dynamic_content import generate_token
from ims.deep_link import deep_link_content, deep_link_frame
# Constants
# DEEPLINK_BODY = 'https://purl.imsglobal.org/spec/lti-dl/claim/deep_linking_settings'
# DEPLOYMENT_ID = 'https://purl.imsglobal.org/spec/lti/claim/deployment_id'
from ims.jwt_management import decode_jwt

from pylti1p3.contrib.flask import (FlaskOIDCLogin, FlaskCacheDataStorage, FlaskRequest, FlaskMessageLaunch)

class DeepLinkingPayloadData(Resource):
    """
    Deeplink payload
    """

    def get(self):
        """
        Get method to obtain the payload from the launch_id
        :param launch_id
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

        token = request_json["token"]
        jwt = cache.get(token)
        lti_content = request_json["deep_link_content"]

        content = deep_link_content(lti_content)

        deep_link_jwt = self.get_message_jwt(jwt, content)
        signed_jwt = self.encode_jwt(deep_link_jwt, jwt['aud'], jwt['iss'])

        return {
            'deep_link_response': deep_link_jwt,
            'signed_jwt': signed_jwt,
            'return_url': jwt['https://purl.imsglobal.org/spec/lti-dl/claim/deep_linking_settings']['deep_link_return_url']
        }

    def get_message_jwt(self, payload, resources):
        deep_link = payload['https://purl.imsglobal.org/spec/lti-dl/claim/deep_linking_settings'];

        message_jwt = {
            'iss': payload['aud'],
            'aud': [payload['iss']],
            'exp': int(time.time()) + 600,
            'iat': int(time.time()),
            'nonce': 'nonce-' + uuid.uuid4().hex,
            'https://purl.imsglobal.org/spec/lti/claim/deployment_id': payload['https://purl.imsglobal.org/spec/lti/claim/deployment_id'],
            'https://purl.imsglobal.org/spec/lti/claim/message_type': 'LtiDeepLinkingResponse',
            'https://purl.imsglobal.org/spec/lti/claim/version': '1.3.0',
            'https://purl.imsglobal.org/spec/lti-dl/claim/content_items': resources,
            'https://purl.imsglobal.org/spec/lti-dl/claim/data': deep_link['data']
        }
        return message_jwt

    def encode_jwt(self, message, client_id, iss):
        headers = None
        jwks = current_app.config['LTI_TOOL_CONFIG'].get_jwks(iss, client_id)
        kid = jwks['keys'][0]['kid']
        private_key = current_app.config['LTI_TOOL_CONFIG'].get_private_key(iss, client_id)
        if kid:
            headers = {'kid': kid}
        encoded_jwt = jwt.encode(message, private_key, algorithm='RS256', headers=headers)
        if sys.version_info[0] > 2 and isinstance(encoded_jwt, bytes):
            return encoded_jwt.decode('utf-8')
        return encoded_jwt

class CustomDeepLinkingContentTypes(Resource):
    """
    Custom deeplinking content
    """

    def get(self):
        """

        :return:
        """

        return get_files_from_bucket()


class DeepLinkingOptions(Resource):
    """
    Deeplink Option
    """

    def post(self):
        """
        Post method
        :return:
        """

        flask_request = FlaskRequest()
        launch_data_storage = FlaskCacheDataStorage(cache)
        message_launch = FlaskMessageLaunch(flask_request, current_app.config['LTI_TOOL_CONFIG'], launch_data_storage=launch_data_storage)
        message_launch_data = message_launch.get_launch_data()
        pprint.pprint(message_launch_data)
        token = message_launch.get_launch_id()
        cache.set(token, message_launch_data)

        redirection = redirect('http://localhost:3000/deepLinkContent/' + token)

        return redirection

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
