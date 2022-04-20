"""
app.apis.internal.config
------------------------

"""
import json
import botocore
from flask import jsonify
from flask_restful import Resource, reqparse, request
from pkg_resources import require
from requests_cache import json_serializer
from helpers import dynamo_client
from config.app_config import DYNAMO_TABLE


class Configuration(Resource):
    """
    Returns the current configuration
    """
    def get(self, tool_config_id):
        """
        Returns an lti_config tool based on the id, if the endpoint returns 500 is because the content from dynamodb is invalid
        :return:
        """
        if(tool_config_id):
            try:
                result = dynamo_client.retrieve_configuration(DYNAMO_TABLE,tool_config_id)
                return result, 200
            except KeyError:
                return {'Error':'The key does not exist'}, 404
        else:
            return {'Error':'Please use a valid string to query'}, 400


    def post(self,tool_config_id):
        """
        Post method to add a new LTI tool configuration file.
        """
        # First receive the values from config
        data = request.get_json()
        if (data and tool_config_id):
            #first we need to put everything together as Dynamo will expect it
            final_item = {
                "tool_config_id":tool_config_id,
                "configurations":data
            }
            # try to create a new value in dynamo
            try:
                result = dynamo_client.create_configuration(final_item, DYNAMO_TABLE)
                return result
            # whenever dynamo returns an error
            except botocore.exceptions.ClientError as error :
                if error.response['Error']['Code'] == 'ValidationException':
                    return {"Error" :"tool_config_id cannot be empty. " + error.response['Error']['Message']},400
            # whenever we detect there is user input error
            except ValueError as error:
                return {'Error': str(error)}, 400
        else:
            return {'Error' : 'Either the configuration or the hash key are empty'}, 400
    
    def put(self, tool_config_id):
        """
        Post method to add a new LTI tool configuration file.
        """
        # First receive the values from config
        data = request.get_json()
        if (data and tool_config_id):
            #first we need to put everything together as Dynamo will expect it
            final_item = {
                "tool_config_id":tool_config_id,
                "configurations":data
            }
            # try to create a new value in dynamo
            try:
                result = dynamo_client.update_configuration(final_item, DYNAMO_TABLE)
                return result
            # whenever dynamo returns an error
            except botocore.exceptions.ClientError as error :
                if error.response['Error']['Code'] == 'ValidationException':
                    return {"Error" :"tool_config_id cannot be empty. " + error.response['Error']['Message']},400
            # whenever we detect there is user input error
            except ValueError as error:
                return {'Error': str(error)}, 400
        else:
            return {'Error' : 'Either the configuration or the hash key are empty'}, 400

    def delete(self, tool_config_id):
            """
            removes the complete line of a tool_config_id
            """
            if(tool_config_id):
                result = dynamo_client.remove_configuration(tool_config_id,DYNAMO_TABLE)
                return result
            else:
                return {'Error':'The tool_config_id or hash_ley is empty'}, 400

class Configurations(Resource):
    """
    LTI tool configuration file for a specific ID
    """

    def get(self):
        """
        Returns the LTI tool configuration of a specific lti_config_id
        """
        result = dynamo_client.retrieve_configuration_id_list(DYNAMO_TABLE)
        return result



class SetupPage(Resource):
    """

    """

    def get(self):
        """

        :return:
        """
        pass


