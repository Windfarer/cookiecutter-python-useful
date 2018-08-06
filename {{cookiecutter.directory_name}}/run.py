import config
from logs import config_logging

# init logging
config_logging(config.LOG_LEVEL)

import logging
logger = logging.getLogger(__name__)

import click


@click.group()
def cli():
    pass

@cli.command()
def hello():
    logger.info("hello.")
    pass


if __name__ == '__main__':
    cli()