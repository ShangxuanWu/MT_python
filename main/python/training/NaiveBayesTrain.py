# Shangxuan Wu @ Myraid of Things
# 23 Jun 2017

import pdb

def main():
    from sklearn import datasets
    iris = datasets.load_iris()
    # format of data:
    # iris.data: N * 4 np.array
    # iris.target: N * 1 np.array
    from sklearn.naive_bayes import GaussianNB
    gnb = GaussianNB()
    # this one can perform online update
    y_pred = gnb.fit(iris.data, iris.target).predict(iris.data)
    pdb.set_trace()
    print("Number of mislabeled points out of a total %d points : %d"
        % (iris.data.shape[0],(iris.target != y_pred).sum()))
    return

if __name__ == "__main__":
    main()