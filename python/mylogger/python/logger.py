import logging
from logging.handlers import RotatingFileHandler
from datetime import datetime


backup = ".\\Backups"
max_size = 1024 * 1024 * 10 # 10 MB
backup_count = 10
file = True

log_formatter = logging.Formatter('%(asctime)s %(levelname)s [%(filename)s -> %(lineno)d]: %(message)s',datefmt='%Y-%m-%dT%H:%M:%S')
path = f'./{datetime.now().strftime("%Y%m%d")}_logfile.txt'

#Setup File handler
file_handler = logging.FileHandler(path)
file_handler.setFormatter(log_formatter)
file_handler.setLevel(logging.INFO)

#Setup Stream Handler (i.e. console)
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(log_formatter)
stream_handler.setLevel(logging.DEBUG)

#setup handler
logger = logging.getLogger("root")
if file:
  logger.addHandler(file_handler)
logger.addHandler(stream_handler)
