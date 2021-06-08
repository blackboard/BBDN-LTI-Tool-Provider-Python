"""

"""
import json

import boto3
from flask import current_app


def get_files_from_bucket():
    """

    :return:
    """
    #
    # s3_file = 's3://contenttypes/deepLinking_contentLink.json'

    s3 = boto3.client('s3', aws_access_key_id=current_app.settings['AWS_KEY_ID'],
                      aws_secret_access_key=current_app.settings['AWS_KEY_ID_SECRET'])

    s3_object = s3.get_object(Bucket='contenttypes', Key='deepLinking_contentLink.json')
    resp = s3_object['Body']

    return json.load(resp)
