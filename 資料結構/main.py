import logging
import logging.config

from os import path
log_file_path = path.join(path.dirname(path.abspath(__file__)), 'loggin.conf')
logging.config.fileConfig(log_file_path)
#
#logging.config.fileConfig('logging.conf')
root_logger = logging.getLogger('root')
root_logger.debug('test root logger...')
 
logger = logging.getLogger('main')
logger.info('test main logger')
logger.info('start import module \'mod\'...')
import mod
 
logger.debug('let\'s test mod.testLogger()')
mod.testLogger()
root_logger.info('finish test...')