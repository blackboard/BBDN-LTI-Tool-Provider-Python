from distutils.log import debug
from decouple import config

PORT = config('PORT', default='5000')
DEBUG = True
DOMAIN = config('DOMAIN', default='127.0.0.1')
SERVER_NAME = DOMAIN + ':' + PORT
FRONTEND_URL = config('FRONTEND_URL', default="http://localhost:3000")
CACHE_CONFIG = {
    'CACHE_TYPE': 'redis',
    'CACHE_DEFAULT_TIMEOUT': config('CACHE_DEFAULT_TIMEOUT', default=300, cast=int),
    'CACHE_REDIS_HOST': config('REDIS_HOST', default='lti_redis.service.local'),
    'CACHE_REDIS_PORT': config('REDIS_PORT', default=6379, cast=int),
    'CACHE_REDIS_URL': config('REDIS_URL', default='redis://lti_redis.service.local:6379/5')
}

# ***** DYNAMODB *****
# This variable defines if you want to run the application using dynamo or locally
# CONFIG_SOURCE receives two values ['LOCAL','DYNAMO']
# LOCAL_CONFIG_PATH receives the location of the file, by default it takes the file in the same path as app_config.py, if CONFIG_SOURCE is DYNAMO, LOCAL_CONFIG_PATH can be empty
# TOOL_CONFIG_ID: This variables takes the primary key of the configuration you want to load in, when using default configuration, you are unable to use the endpoints.
CONFIG_SOURCE = 'DYNAMO'
# needs to be a full path
LOCAL_CONFIG_PATH = '/Users/dherrera/Documents/Projects/ltiTestingTool/BBDN-LTI-Tool-Provider-Python/app/config/tool_config.json'
# when using default configuration, set thos variable to default
TOOL_CONFIG_ID = 'ab1ab1'

# Do not modify the following values
# DEFAULT_DYNAMO_TABLE sets the default table for the default values (read only)
DEFAULT_DYNAMO_TABLE = 'tool_config_default'
# DYNAMO_TABLE is the table that stores the configurations that can be managed
DYNAMO_TABLE = 'tool_config'
# DYNAMO_HASH_KEY_NAME Defines the primary key name to be used to call the configs
DYNAMO_HASH_KEY_NAME = 'tool_config_id'

# AWS Connection
AWS_KEY_ID = config('AWS_KEY_ID', default='ASIA4XODGDVQANTWEFG3')
AWS_KEY_ID_SECRET = config('AWS_KEY_ID_SECRET', default='0euN5P9TRXJD9xeq0pihghvfXxMMQUCaPrZS5qug')

# Dynamo config
