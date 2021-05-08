"""
app.ims.lti_advantage
---------------------

"""
from logging import Logger

from py_jwt_validator import PyJwtValidator, PyJwtException


def verify_token(id_token, jwt_payload, setup) -> bool:
    """

    :param id_token:
    :param jwt_payload:
    :param setup:
    :return:
    """
    parts = id_token.split('.')

    try:
        PyJwtValidator(id_token)
    except PyJwtException as e:
        Logger.error('Exception caught. Error: %s', e, log_level=1)
        return False

    return True
