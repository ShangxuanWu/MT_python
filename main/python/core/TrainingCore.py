# Copyright: Shangxuan Wu @ Myraid of Things
# 20 Jun 2017

import tensorflow as tf
import pdb, argparse, logging

def getParams():
    return params

def evaluate():
    return

def train(params):
    if params['AlgorithmType'] == 'MLP':

    elif params['AlgorithmType'] == 'NB':
        
    else:
        raise NotImplementedError
    return

def tryLogger():
    logger.warning("AAA")
    logger.error("AAA")
    pass






if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    logger.info("Main python code for Myraid of Things.")
    tryLogger()

    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+',
                   help='an integer for the accumulator')
    parser.add_argument('--sum', dest='accumulate', action='store_const',
                   const=sum, default=max,
                   help='sum the integers (default: find the max)')

    args = parser.parse_args()
    print(args.accumulate(args.integers))
    pass