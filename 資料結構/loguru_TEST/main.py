
from loguru import logger

logger.remove()
logger.add('muti.log',enqueue=True)
logger.debug('test root logger...')

logger.debug('test main logger')

logger.info('start import module \'mod\'...')
import mod
 
logger.debug('let\'s test mod.testLogger()')
mod.testLogger()
logger.info('finish test...')