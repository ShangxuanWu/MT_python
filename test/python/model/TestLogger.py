# CopyRight Shangxuan Wu @ Myriad of Things
# 02 Feb 2018

# This test script is for testing the logger functions.

import logging

logger = logging.getLogger("this class")
logger.setLevel(logging.DEBUG)

# print in screen
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

# output to file



logger.debug("logger working")

try:
    assert 1 == 0
except AssertionError as err:
    logger.exception("My assert failed :( ")
    raise err

print("aaaaaaaaa")