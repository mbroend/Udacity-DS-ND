import logging

logging.basicConfig(filename='logs3.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s',level=logging.DEBUG)

logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')
