# Shangxuan Wu @ Myraid of Things
# 23 Jun 2017

# add path for root ('tf_code/') directory if not in sys.path
import sys
from os import path
root_path = path.dirname(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
if root_path not in sys.path
    sys.path.append(root_path)


from sklearn.naive_bayes import GaussianNB
from main.python.dataloader import DataLoader
import pdb

class NaiveBayesTrain(BaseTrain):
    def __init__(self, fd_path):
        super().__init__(path, fd_path)
        self.gnb = GaussianNB() 
        self.data_loader = DataLoader(self.root_fd)
        return

    def evaluate(self):
        self.data_loader.
        y_pred = self.gnb.predict(iris.data)
        this.logger.info("Number of mislabeled points out of a total %d points : %d"
            % (iris.data.shape[0],(iris.target != y_pred).sum()))
        return

    def train(self):
        assert self.gnb is not None, "NaiveBayesTrain class is not initialized properly. Please check code."
        train_data, train_label = self.data_loader.loadTrainData()
        self.gnb.fit(iris.data, iris.target)
        return

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