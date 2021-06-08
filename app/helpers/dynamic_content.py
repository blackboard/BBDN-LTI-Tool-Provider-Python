"""
app.helpers.dynamic_content
---------------------------

"""

import hashlib
import json


def generate_token(json_object: (dict, list)):
    """
    This function returns a token calculated on the object itself
    :arg json_object is the jsonObject to generate the token
    :return: Hash MD5 on the json object
    """

    return hashlib.md5(json.dumps(json_object).encode("utf-8")).hexdigest()
