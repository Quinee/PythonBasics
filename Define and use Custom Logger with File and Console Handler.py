import logging
logger =logging.getLogger('demoLogger')
logger.setLevel(logging.DEBUG)
consoleHandler=logging.StreamHandler()
fileHandler=logging.FileHandler('filehandler.log',mode='w')
formatter=logging.Formatter('%(asctime)s:%(levelname)s:%(process)s:%(lineno)s:%(name)s:%(message)s:%(module)s',datefmt='%d/%m/%Y %I:%M:%S %p')
consoleHandler.setFormatter(formatter)
fileHandler.setFormatter(formatter)
logger.addHandler(consoleHandler)
logger.addHandler(fileHandler)
logger.critical('It is critical msg')
logger.error('It is error msg')
logger.warning('It is warning msgg')
logger.info('It is info msg')
logger.debug('It is debug msg')