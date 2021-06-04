"""
app.internal.ims.lti_11
-----------------------

"""

from flask_restful import Resource
from flask import request

CONTENT_ITEM_SELECTION_REQUEST = "ContentItemSelectionRequest"


class Lti(Resource):
    """

    """

    def post(self):
        """

        :return:
        """
        if request.data.lti_message_type == CONTENT_ITEM_SELECTION_REQUEST:
            pass




class Membership(Resource):
    """

    """

    def get(self):
        """

        :return:
        """
        pass
