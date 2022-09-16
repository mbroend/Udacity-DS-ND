import logging

logger = logging.getLogger()
logger.setLevel(logging.NOTSET)

# our first handler is a console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.ERROR)
console_handler_format = '%(asctime)s | %(levelname)s: %(message)s'
console_handler.setFormatter(logging.Formatter(console_handler_format))
logger.addHandler(console_handler)

# the second handler is a file handler
file_handler = logging.FileHandler('logs4.log')
file_handler.setLevel(logging.INFO)
file_handler_format = '%(asctime)s | %(levelname)s | %(lineno)d: %(message)s'
file_handler.setFormatter(logging.Formatter(file_handler_format))
logger.addHandler(file_handler)

# start logging and show messages
logger.debug('Here you have some information for debugging.')
logger.info('Everything is normal. Relax!')
logger.warning('Something unexpected but not important happend.')
logger.error('Something unexpected and important happened.')
logger.critical('OMG!!! A critical error happend and the code cannot run!')