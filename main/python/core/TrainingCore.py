# Copyright: Shangxuan Wu @ Myraid of Things
# 20 Jun 2017

# add path for root ('tf_code/') directory if not in sys.path
import sys
from os import path
root_path = path.dirname(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
if root_path not in sys.path
    sys.path.append(root_path)

from main.python.model import MLPModel, NBModel, LSTMModel, RNNModel
import pdb, argparse, logging

def getParams():
    return params

def evaluate(data_fd):
    if params['AlgorithmType'] == 'MLP':
        algorithm = MLPModel.MLP(data_fd)
    elif params['AlgorithmType'] == 'NaiveBayes':
        algorithm = NaiveBayesModel.NaiveBayes(data_fd)
    elif params['AlgorithmType'] == 'RNN':
        algorithm = RNNModel.RNN(data_fd)
    elif params['AlgorithmType'] == 'LSTM':
        algorithm = LSTMModel.LSTM(data_fd)
    else:
        raise NotImplementedError
    algorithm.evaluate()
    return

def train(params):
    if params['AlgorithmType'] == 'MLP':
        algorithm = MLPModel.MLP(data_fd)
    elif params['AlgorithmType'] == 'NaiveBayes':
        algorithm = NaiveBayesModel.NaiveBayes(data_fd)
    elif params['AlgorithmType'] == 'RNN':
        algorithm = RNNModel.RNN(data_fd)
    elif params['AlgorithmType'] == 'LSTM':
        algorithm = LSTMModel.LSTM(data_fd)
    else:
        raise NotImplementedError
    algorithm.train()
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