# This second line must remain commented ONLY when using Dynamo, if using local json file, remove the #
# from app.config.app_config import DYNAMO_HASH_KEY_NAME
import boto3
import botocore.exceptions

# Globals
# define the usage of dynamodb as the boto resource
dynamodb = boto3.resource('dynamodb')
# defining conditional expressions
attribute_exists = 'attribute_exists(tool_config_id)'
attribute_not_exists = 'attribute_not_exists(tool_config_id)'

# Create config only creates it if it does not exist, primary keys cannot be updated.
def create_configuration(new_configuration:dict, table_name:str):
            table = dynamodb.Table(table_name)
            # update boolean is evaluated
            try:
                table.put_item(
                    Item= new_configuration,
                    ConditionExpression=attribute_not_exists
                )
                return {'Success':'Record will eventually be created'}, 202
                # since there is a condition we need to return either values
            except botocore.exceptions.ClientError:
                return {"Error": "You are trying to create a configuration using a primary key that already exists, please use update to rewrite an existing configuration"}, 400

# this is basically the same function as create configuration, however I separated them because it became a bit unreadable and added new condition expressions to each
def update_configuration(new_configuration:dict, table_name:str):
            table = dynamodb.Table(table_name)
            # update boolean is evaluated
            try:
                table.put_item(
                    Item= new_configuration,
                    ConditionExpression=attribute_exists
                )
                return {'Success':'Record will eventually be updated'}, 202
                # since there is a condition we need to return either values
            except botocore.exceptions.ClientError:
                return {"Error": "You are trying to update a configuration that does not exist, please use create to generate a new configuration"}, 400

# returns a configuration
def retrieve_configuration(hash_key:str,table_name:str):  
    if(table_name and hash_key):
        table = dynamodb.Table(table_name)
        response = table.get_item(
            Key={
                'tool_config_id': hash_key
            }
        )
        item = response['Item']
        return item


# regardless the table is empty this returns a dict with empty results
def retrieve_configuration_id_list(table_name:str):
    table = dynamodb.Table(table_name)  
    response = table.scan(
        ProjectionExpression = 'tool_config_id'
    )
    # receive the items as a list with dictionaries but all of them have the same keys
    item_list = []
    response_list = response['Items']
    for i,item in enumerate(response_list):
        item_list.append(item['tool_config_id'])

    item_dict = {
        'tool_config_id' : item_list
    }
    return item_dict,200


def remove_configuration(hash_key:str,table_name:str):
    if(table_name and hash_key):
        table = dynamodb.Table(table_name)
        try:
            table.delete_item(
                Key={
                    'tool_config_id': hash_key
                }, 
                ConditionExpression=attribute_exists
            )
            return {"message:": "Value has been removed"},200
        except botocore.exceptions.ClientError:
            return {"error:": "tool_config_id does not exist"},404
