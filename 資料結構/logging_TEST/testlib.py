
import logging

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


def foo():
    logger.info('info: this is foo message')
    print('print: foo')