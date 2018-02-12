import logging


# Please call this function only once in the start of main()
# @input: output_file_name: full path of output file name
def initializeLogger(output_file_name):
    # define loggers
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # Logger1: print in screen
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    # Logger2: output to file
    fh = logging.FileHandler(output_file_name)
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    return

# A quick hack of outputting assert exceptions to file
def loggedAssert(logger, expression):
    try:
        assert expression
    except AssertionError as err:
        logger.exception("My assert failed :( ")
        raise err