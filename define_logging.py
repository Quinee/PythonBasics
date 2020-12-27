import logging
#logging.basicConfig(filename='log.txt',level=logging.WARNING,filemode='w')
#Format the log msg
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(process)s:%(lineno)s:%(name)s:%(message)s:%(module)s',datefmt='%d/%m/%y %I:%M:%S %p')
logging.warning('This is warning')
logging.critical('This is critical')
#Add time and date to log msg
