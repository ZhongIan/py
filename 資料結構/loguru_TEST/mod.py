
from loguru import logger
import submod

logger.info('logger of mod say something...')
 
def testLogger():
    logger.debug('this is mod.testLogger...')
    submod.tst()