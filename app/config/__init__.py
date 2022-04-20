"""
conf/__init__.py
-------------------------------------------------------------------
"""

from distutils.log import error
from webbrowser import get
from pylti1p3.tool_config import ToolConfDict, ToolConfJsonFile
from app.config.app_config import CONFIG_SOURCE, LOCAL_CONFIG_PATH, TOOL_CONFIG_ID, DYNAMO_TABLE, DEFAULT_DYNAMO_TABLE
from helpers import dynamo_client
from config import app_config

def init_app(app): 
    """
    :param app:
    :return:
    """
    pass

class Settings:
    def __init__(self):
        for setting in dir(app_config):
            setattr(self, setting, getattr(app_config, setting))
            if(CONFIG_SOURCE == "LOCAL"):
                ## Settings when using a local config
                setattr(self, "LTI_TOOL_CONFIG", ToolConfJsonFile(LOCAL_CONFIG_PATH))
            elif(CONFIG_SOURCE == "DYNAMO" and TOOL_CONFIG_ID == "default"):
                setattr(self, "LTI_TOOL_CONFIG", ToolConfDict(dynamo_client.retrieve_configuration('default',DEFAULT_DYNAMO_TABLE)['configurations']))
            elif(CONFIG_SOURCE == "DYNAMO" and TOOL_CONFIG_ID != "default" or TOOL_CONFIG_ID != ""):
                setattr(self, "LTI_TOOL_CONFIG", ToolConfDict(dynamo_client.retrieve_configuration(TOOL_CONFIG_ID,DYNAMO_TABLE)['configurations']))
            else:
                print('error')
        

settings = Settings()
