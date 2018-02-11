# Shangxuan Wu @ Myraid of Things
# 23 Jun 2017

'''
Jave code reference:

case MT_STRATEGY_NAIVE_BAYES:
            tradingConfigDto.setNbPredictionPeriod(modelLearningProperties.getNbPredictionPeriod());
            tradingConfigDto
                    .setNbPositiveCorrelationCoefficient(modelLearningProperties.getNbPositiveCorrelationCoefficient());
            tradingConfigDto
                    .setNbNegativeCorrelationCoefficient(modelLearningProperties.getNbNegativeCorrelationCoefficient());

            break;

'''

# add path for root ('tf_code/') directory if not in sys.path
import sys, os
root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
if root_path not in sys.path
    sys.path.append(root_path)

from sklearn.naive_bayes import GaussianNB
import pdb
import cPickle
from main.python.utils import FileUtils
from main.python.dataloader import DataLoader
import Base

class NaiveBayesModel(BaseModel):
    def __init__(self, fd_path):
        super().__init__(path, fd_path)
        self.gnb = GaussianNB() 
        self.data_loader = DataLoader(self.root_fd)
        self.logger = 
        return

    def evaluate(self):
        self.data_loader.loadT
        y_pred = self.gnb.predict(iris.data)
        self.logger.info("Number of mislabeled points out of a total %d points : %d"
            % (iris.data.shape[0],(iris.target != y_pred).sum()))
        return

    def train(self):
        assertToLogger(self.gnb is not None, "NaiveBayesTrain class is not initialized properly. Please check code.")
        train_data, train_label = self.data_loader.loadTrainData()
        self.gnb.fit(iris.data, iris.target)
        return

    # Saving model into `./model/` folder.
    def saveModel(self):
        full_model_path = os.path.join(self.model_fd, 'nb_classifier.pkl')
        with open(full_model_path, 'wb') as fid:
            cPickle.dump(self.gnb, fid)  
        self.logger.info('Naive Bayes model saved!')
        return
    
    # Loading model from `./model/` folder.
    def loadModel(self):
        full_model_path = os.path.join(self.model_fd, 'nb_classifier.pkl')        
        assert FileUtils.isFileExists(full_model_path)
        with open(full_model_path, 'rb') as fid:
            self.gnb = cPickle.load(fid)
        self.logger.info('Naive Bayes model loaded!')
        return