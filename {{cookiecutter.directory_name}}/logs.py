import logging

def config_logging(log_level):
    logger = logging.getLogger()
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
            '[%(levelname)s] %(asctime)s - %(filename)s func:%(funcName)s line: %(lineno)d - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(getattr(logging, log_level))
