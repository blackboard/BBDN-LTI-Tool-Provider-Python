"""
conf/__init__.py
-------------------------------------------------------------------
"""
from logging import Logger, INFO
from pathlib import Path

from pylti1p3.tool_config import ToolConfJsonFile

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

        path = Path(__file__).absolute().parent

        setattr(self, "LTI_TOOL_CONFIG", ToolConfJsonFile(path / "tool_config.json"))


settings = Settings()

