"""
app.ims.jwt_management
----------------------

"""

import json

import jwt
import requests
from flask import current_app


def decode_jwt(jwt_token, provider):
    """

    :param jwt_token:
    :param provider:
    :return:
    """

    jwks_url = current_app.config['LTI_TOOL_CONFIG'].get_iss_config(provider)['key_set_url']
    jwks = requests.get(jwks_url).json()

    public_keys = {}
    for jwk in jwks['keys']:
        kid = jwk['kid']
        public_keys[kid] = jwt.algorithms.RSAAlgorithm.from_jwk(json.dumps(jwk))

    kid = jwt.get_unverified_header(jwt_token)['kid']
    key = public_keys[kid]

    jwt_payload = jwt.decode(jwt_token, key=key, audience='5d678c4f-7ad1-47b3-811b-b389950a3ef5', algorithms=['RS256'])

    return jwt_payload