# Shangxuan Wu @ Myraid of Things
# 20 Jun 2017

''' TODO: support the following features:
- crossvalidation
- no regularization
- activation function

Java code Reference:

case MT_STRATEGY_MLP:
            tradingConfigDto.setMlpNumberOfEpochs(modelLearningProperties.getMlpNumberOfEpochs());
            tradingConfigDto.setMlpNumberOfLayers(modelLearningProperties.getMlpNumberOfLayers());
            tradingConfigDto.setMlpNumberOfHiddenLayers(modelLearningProperties.getMlpNumberOfHiddenLayers());
            tradingConfigDto.setMlpNumberOfInputNodes(modelLearningProperties.getMlpNumberOfInputNodes());
            tradingConfigDto.setMlpNumberOfHiddenNodes(modelLearningProperties.getMlpHiddenNodesStr());
            tradingConfigDto.setMlpNumberOfOutputNodes(modelLearningProperties.getMlpNumberOfOutputNodes());
            tradingConfigDto.setMlpLearningRate(modelLearningProperties.getMlpLearningRate());
            tradingConfigDto.setMlpNumberOfIterations(modelLearningProperties.getMlpNumberOfIterations());
            tradingConfigDto.setMlpMaximumErrors(modelLearningProperties.getMlpMaximumErrors());
            tradingConfigDto.setMlpMinimumAccuracy(modelLearningProperties.getMlpMinimumAccuracy());
            tradingConfigDto.setMlpPredictionPeriod(modelLearningProperties.getMlpPredictionPeriod());
            tradingConfigDto.setMlpEfficientPercentage(modelLearningProperties.getMlpEfficientPercentage());
            tradingConfigDto.setMlpDataProcessMode(modelLearningProperties.getMlpDataProcessMode());

            if (tradingConfigDto.getMlpDataProcessMode().equals(MT_STRATEGY_MLP_DATA_PROCESS_MODE_PARTITION)
                    || tradingConfigDto.getMlpDataProcessMode()
                            .equals(MT_STRATEGY_MLP_DATA_PROCESS_MODE_PARTITIONALL)) {
                tradingConfigDto.setMlpPartitionSize(modelLearningProperties.getMlpPartitionSize());
            }

            tradingConfigDto.setMlpClassifierBuildingMode(modelLearningProperties.getMlpClassifierBuildingMode());
            tradingConfigDto.setMlpSeed(modelLearningProperties.getMlpSeed());

            break;

'''

# add path for root ('tf_code/') directory if not in sys.path
import sys, os
root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
if root_path not in sys.path
    sys.path.append(root_path)

from __future__ import absolute_import, division, print_function
from six.moves.urllib.request import urlopen
import tensorflow as tf
import numpy as np
import sys, argparse, os
import pdb
from main.python.utils import FileUtils
from main.python.dataloader import DataLoader
import Base

class MLPModel(BaseModel):
    def __init__(self, path, time_str):
        super().__init__(path, time_str, __name__)
        '''[]
        Build 3 layer DNN with 10, 20, 10 units respectively.
        The default construction parameters are

        __init__(
            hidden_units,
            feature_columns,
            model_dir=None,
            n_classes=2,
            weight_column=None,
            label_vocabulary=None,
            optimizer='Adagrad',
            activation_fn=tf.nn.relu,
            dropout=None,
            input_layer_partitioner=None,
            config=None
        )

        with self-adapting learning rates in AdaGrad.
        '''
        self.classifier = tf.estimator.DNNClassifier(
            feature_columns=feature_columns,
            hidden_units=[10, 20, 10],
            n_classes=3,
            model_dir=self.model_fd
            )
        return

    def parseParameters(self):


        return params

    def loadModel(self):
        return
    
    def saveModel(self):
        self.classifier.export_savedmodel(self.model_fd, serving_input_receiver_fn)
        return

    def evaluate(self):
        assert this.classifier is not None, "MLPTrain class is not initialized properly. Please check code."        
        # evaluate accuracy
        accuracy_score = this.classifier.evaluate(input_fn=test_input_fn)["accuracy"]
        print("\nTest Accuracy: {0:f}\n".format(accuracy_score))
        # log here
        
        return

    def train(self, data, label):
        assert this.classifier is not None, "MLPTrain class is not initialized properly. Please check code."
        # train model, automatically saving all the ckpts
        this.classifier.train(input_fn=train_input_fn, steps=2000)
        # should call the update function here
        return

    def forward(self):

        return