import time
import logging
import os
import datetime

log_file = 'app.log'
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(lineno)d %(message)s'
)

abs_path = os.path.abspath(log_file)
file_size = os.path.getsize(log_file)


creation_time = os.path.getctime(log_file)
creation_timestamp = datetime.datetime.fromtimestamp(creation_time)


# current_time = time.localtime()
# time = time.strftime("%y-%m-%d %H:%M:%S", current_time)
# print(time)
