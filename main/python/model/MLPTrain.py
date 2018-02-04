# Shangxuan Wu @ Myraid of Things
# 20 Jun 2017

''' TODO: support the following features:
- crossvalidation
- no regularization
- activation function
'''

from __future__ import absolute_import, division, print_function
from six.moves.urllib.request import urlopen
import tensorflow as tf
import numpy as np
import sys, argparse, os
import pdb
import BaseTrain

class MLPTrain(BaseTrain):
    def __init__(self, path, time_str):
        super().__init__(path, time_str, __name__)
        # build 3 layer DNN with 10, 20, 10 units respectively
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