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

    provider_config = current_app.config['LTI_TOOL_CONFIG'].get_iss_config(provider)
    jwks_url = provider_config['key_set_url']
    jwks = requests.get(jwks_url).json()

    public_keys = {}
    for jwk in jwks['keys']:
        kid = jwk['kid']
        public_keys[kid] = jwt.algorithms.RSAAlgorithm.from_jwk(json.dumps(jwk))

    kid = jwt.get_unverified_header(jwt_token)['kid']
    key = public_keys[kid]

    jwt_payload = jwt.decode(jwt_token, key=key, audience=provider_config['client_id'], algorithms=['RS256'])

    return jwt_payload