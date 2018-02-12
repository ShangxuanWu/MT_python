# CopyRight Shangxuan Wu @ Myriad of Things
# 02 Feb 2018

# This simple test script is for testing the logger functions.
# It outputs to the console, as well as a file 'TestLoggerResult.txt'
# We can manually check the output file.

# add path for root ('tf_code/') directory if not in sys.path
import sys, os
root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
if root_path not in sys.path:
    sys.path.append(root_path)

import logging, pdb
from main.python.utils import FileUtils, LogUtils

# Variables
output_file_name = 'test/python/utils/TestLogUtilsResult.txt'

# Delete if exist
FileUtils.deleteFileIfExist(output_file_name)

# Initialize a logger
LogUtils.initializeLogger(output_file_name)

# # define loggers
# logger = logging.getLogger("this class")
# logger.setLevel(logging.DEBUG)

# # Logger1: print in screen
# ch = logging.StreamHandler()
# ch.setLevel(logging.DEBUG)
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# ch.setFormatter(formatter)
# logger.addHandler(ch)

# # Logger2: output to file
# fh = logging.FileHandler(output_file_name)
# fh.setLevel(logging.DEBUG)
# fh.setFormatter(formatter)
# logger.addHandler(fh)

logger = logging.getLogger("TEST")

# Normal debugging log
logger.debug("logger working")

# Assertion log
LogUtils.loggedAssert(logger, 1==0)

# Assertion log
# try:
#    assert 1 == 0
# except AssertionError as err:
#    logger.exception("My assert failed :( ")
#    raise err

print("Test script reaches here!")