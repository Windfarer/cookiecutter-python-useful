"""
All environments located here
"""
import logging

logger = logging.getLogger(__name__)

from os import getenv


def get_env(env_name, default=None, required=False, arg_formatter=None):
    rv = getenv(env_name)
    if required and rv is None and default is None:
        raise ValueError("'{}' environment variable is required.".format(env_name))
    elif rv is None:
        logger.warning("'{}' uses default value: {}".format(env_name, default))
        rv = default
    if arg_formatter is not None:
        rv = arg_formatter(rv)
    return rv

# global settings

LOG_LEVEL = get_env("LOG_LEVEL", "INFO")
