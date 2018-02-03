# CopyRight Shangxuan Wu @ Myriad of Things
# 2 Feb 2018

# add path for root ('tf_code/') directory if not in sys.path
import sys
from os import path
root_path = path.dirname(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
if root_path not in sys.path
    sys.path.append(root_path)

import main.python.training.NaiveBayesTrain
import pdb

def main():
    from sklearn import datasets
    iris = datasets.load_iris()
    # format of data:
    # iris.data: N * 4 np.array
    # iris.target: N * 1 np.array
    
    nb_train = NaiveBayesTrain()
    nb_train.train()
    nb_train.evaluate()
    return

if __name__ == "__main__":
    main()