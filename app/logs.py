"""
app.logs
--------

"""

import logging


def setup_logger(name, log_file, level=logging.INFO, format=None) -> logging.Logger:
    """

    :param name:
    :param log_file:
    :param level:
    :param format:
    :return:
    """
    logger = logging.getLogger(name)
    if format is None:
        format = '%(asctime)s : %(message)s'
    formatter = logging.Formatter(format)
    file_handler = logging.FileHandler('logs/' + log_file, mode="a")
    file_handler.setFormatter(formatter)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    logger.setLevel(level)
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger


server_logger = setup_logger('server', 'server.log')
api_logger = setup_logger('api', 'api.log', format='%(asctime)-15s %(clientip)s %(path)s %(user)-8s %(message)s')
