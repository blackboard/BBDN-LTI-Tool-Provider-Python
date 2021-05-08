"""
app.ims.deep_link
-----------------

"""
import json
from logging import Logger
from pathlib import Path

from flask import Request

CONTENT_TYPE_STR = 'content_type'
AMOUNT_TYPE_STR = 'amount'

DEEPLINKING_LTI_LINK = 'lti_link'
DEEPLINKING_LTI_LINK_EMBEDDED = 'lti_link_embedded'
DEEPLINKING_LTI_LINK_NEW_WINDOW = 'lti_link_new_window'
DEEPLINKING_LTI_LINK_CONTENT = 'lti_link_content'
DEEPLINKING_LTI_LINK_FILE = 'lti_link_file'
DEEPLINKING_LTI_LINK_HTML = 'lti_link_html'
DEEPLINKING_LTI_LINK_IMAGE = 'lti_link_image'

DEPLOYMENT_ID = 'https://purl.imsglobal.org/spec/lti/claim/deployment_id'
DEEPLINK_BODY = 'https://purl.imsglobal.org/spec/lti-dl/claim/deep_linking_settings'


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
        if content[CONTENT_TYPE_STR] == DEEPLINKING_LTI_LINK:
            items.extend([generate_deep_linking_lti_link() for i in range(content[AMOUNT_TYPE_STR])])
        elif content[CONTENT_TYPE_STR] == DEEPLINKING_LTI_LINK_NEW_WINDOW:
            items.extend([generate_deep_linking_lti_link(new_window=True) for i in range(content[AMOUNT_TYPE_STR])])
        elif content[CONTENT_TYPE_STR] == DEEPLINKING_LTI_LINK_EMBEDDED:
            items.extend([generate_deep_linking_lti_link(embedded=True) for i in range(content[AMOUNT_TYPE_STR])])
        elif content[CONTENT_TYPE_STR] == DEEPLINKING_LTI_LINK_CONTENT:
            items.extend([generate_deep_linking_lti_link(content=True) for i in range(content[AMOUNT_TYPE_STR])])
        elif content[CONTENT_TYPE_STR] == DEEPLINKING_LTI_LINK_HTML:
            items.extend([generate_deep_linking_html() for i in range(content[AMOUNT_TYPE_STR])])
        elif content[CONTENT_TYPE_STR] == DEEPLINKING_LTI_LINK_FILE:
            items.extend([generate_deep_linking_file() for i in range(content[AMOUNT_TYPE_STR])])
        elif content[CONTENT_TYPE_STR] == DEEPLINKING_LTI_LINK_IMAGE:
            items.extend([generate_deep_linking_file(image=True) for i in range(content[AMOUNT_TYPE_STR])])

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
    pass


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
