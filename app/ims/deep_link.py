"""
app.ims.deep_link
-----------------

"""

import datetime
import json
from logging import Logger
from pathlib import Path

from flask import Request, current_app

CONTENT_TYPE_STR = 'content_type'
AMOUNT_STR = 'amount'

DEEPLINK_LTI_LINK = 'lti_link'
DEEPLINK_LTI_LINK_EMBEDDED = 'lti_link_embedded'
DEEPLINK_LTI_LINK_NEW_WINDOW = 'lti_link_new_window'
DEEPLINK_LTI_LINK_CONTENT = 'lti_link_content'
DEEPLINK_LTI_LINK_FILE = 'lti_link_file'
DEEPLINK_LTI_LINK_HTML = 'lti_link_html'
DEEPLINK_LTI_LINK_IMAGE = 'lti_link_image'

DEPLOYMENT_ID = 'https://purl.imsglobal.org/spec/lti/claim/deployment_id'
DEEPLINK_BODY = 'https://purl.imsglobal.org/spec/lti-dl/claim/deep_linking_settings'
DEEPLINK_MESSAGE_TYPE = 'https://purl.imsglobal.org/spec/lti/claim/message_type'
DEEPLINK_VERSION = 'https://purl.imsglobal.org/spec/lti/claim/version'
DEEPLINK_DATA = 'https://purl.imsglobal.org/spec/lti-dl/claim/data'
DEEPLINK_CONTENT_ITEMS = 'https://purl.imsglobal.org/spec/lti-dl/claim/content_items'

def deep_link(request: Request, payload, setup):
    """

    :param request:
    :param payload:
    :param setup:
    :return:
    """
    deploy = payload.body[DEPLOYMENT_ID]
    deep_link_body = payload.body[DEEPLINK_BODY]

    data = deep_link_body.data
    iss = payload.body.iss
    items = list()

    Logger.log('Custom option: {custom_option}'.format(custom_option=request.data.custom_option))
    Logger.log('Custom ims links: {lti_links}'.format(lti_links=request.data.custom_ltilinks))
    Logger.log('Custom embedded ims links: {embedded_links}'.format(embedded_links=request.data.embed_ltilinks))


def deep_link_content(lti_content: list) -> list:
    """

    :param lti_content:
    :return:
    """
    items = list()
    for content in lti_content:
        amount = content[AMOUNT_STR]
        if type(content[AMOUNT_STR]) is str:
            amount = int(content[AMOUNT_STR])

        if content[CONTENT_TYPE_STR] == DEEPLINK_LTI_LINK:
            items.extend([generate_deep_linking_lti_link() for i in range(amount)])
        elif content[CONTENT_TYPE_STR] == DEEPLINK_LTI_LINK_NEW_WINDOW:
            items.extend([generate_deep_linking_lti_link(new_window=True) for i in range(amount)])
        elif content[CONTENT_TYPE_STR] == DEEPLINK_LTI_LINK_EMBEDDED:
            items.extend([generate_deep_linking_lti_link(embedded=True) for i in range(amount)])
        elif content[CONTENT_TYPE_STR] == DEEPLINK_LTI_LINK_CONTENT:
            items.extend([generate_deep_linking_lti_link(content=True) for i in range(amount)])
        elif content[CONTENT_TYPE_STR] == DEEPLINK_LTI_LINK_HTML:
            items.extend([generate_deep_linking_html() for i in range(amount)])
        elif content[CONTENT_TYPE_STR] == DEEPLINK_LTI_LINK_FILE:
            items.extend([generate_deep_linking_file() for i in range(amount)])
        elif content[CONTENT_TYPE_STR] == DEEPLINK_LTI_LINK_IMAGE:
            items.extend([generate_deep_linking_file(image=True) for i in range(amount)])

    return items


def deep_link_frame(iss, aud, deploy, data, items):
    """

    :param iss:
    :param aud:
    :param deploy:
    :param data:
    :param items:
    :return:
    """
    now = datetime.now()

    frame = {
        'iss': iss,
        'aud': aud,
        'sub': iss,
        'ist': now,
        'exp': now + datetime.timedelta(hours=5),
        'locale': "en_US",
        DEPLOYMENT_ID: deploy,
        DEEPLINK_MESSAGE_TYPE: "LtiDeepLinkingResponse",
        DEEPLINK_VERSION: "1.3.0",
        DEEPLINK_DATA: data,
        DEEPLINK_CONTENT_ITEMS: items
    }

    return frame


def generate_deep_linking_lti_link(**kwargs) -> dict:
    """

    :return:
    """
    path = Path(__file__).absolute().parent
    file_location = "responses/deepLinking_ltiLink.json"
    with open(path / file_location) as file:
        link = json.load(file)

    file.close()

    return link


def generate_deep_linking_html() -> dict:
    """

    :return:
    """
    pass


def generate_deep_linking_file(**kwargs) -> dict:
    """

    :return:
    """
    pass
