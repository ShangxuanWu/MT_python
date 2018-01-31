# Shangxuan Wu @ Myraid of Things
# 23 Jun 2017

from sklearn.naive_bayes import GaussianNB
import pdb

class NaiveBayesTrain(BaseTrain):
    def __init__(self, path, time_str):
        super().__init__(path, time_str)
        self.gnb = GaussianNB()
        return

    def evaluate(self):
        y_pred = self.gnb.predict(iris.data)
        print("Number of mislabeled points out of a total %d points : %d"
            % (iris.data.shape[0],(iris.target != y_pred).sum()))
        return

    def train(self):
        assert self.gnb is not None, "NaiveBayesTrain class is not initialized properly. Please check code."
        self.gnb.fit(iris.data, iris.target)
        return

def main():
    from sklearn import datasets
    iris = datasets.load_iris()
    # format of data:
    # iris.data: N * 4 np.array
    # iris.target: N * 1 np.array
    
    # this one can perform online update
    return

if __name__ == "__main__":
    main()