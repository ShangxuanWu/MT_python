import logging

# A quick hack of outputting assert exceptions to file
def loggedAssert(expression):
    try:
        assert expression
    except AssertionError as err:
        logger.exception("My assert failed :( ")
        raise err