import logging
from config.config import *
setup_logging()
logger = logging.getLogger("root")
if __name__ == '__main__':
    logger.info("this is a demo")
    logger.error("this is a error")

