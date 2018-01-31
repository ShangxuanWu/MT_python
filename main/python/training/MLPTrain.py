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

class MLPTrain(BaseTrain):
    def __init__(self):
        # build 3 layer DNN with 10, 20, 10 units respectively
        this.classifier = tf.estimator.DNNClassifier(feature_columns=feature_columns,
                                                hidden_units=[10, 20, 10],
                                                n_classes=3,
                                                model_dir="/tmp/iris_model")
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
        # train model
        this.classifier.train(input_fn=train_input_fn, steps=2000)
        # should call the update function here
        return

def main():
    # Data sets
    DATASET_PATH = "dataset"

    IRIS_TRAINING = os.path.join(DATASET_PATH, "iris_training.csv")
    IRIS_TRAINING_URL = "http://download.tensorflow.org/data/iris_training.csv"

    IRIS_TEST = os.path.join(DATASET_PATH, "iris_test.csv")
    IRIS_TEST_URL = "http://download.tensorflow.org/data/iris_test.csv"

    # If the training and test sets aren't stored locally, download them.
    if not os.path.exists(IRIS_TRAINING):
        raw = urlopen(IRIS_TRAINING_URL).read()
        with open(IRIS_TRAINING, "wb") as f:
            f.write(raw)

    if not os.path.exists(IRIS_TEST):
        raw = urlopen(IRIS_TEST_URL).read()
        with open(IRIS_TEST, "wb") as f:
            f.write(raw)

    # Load datasets.
    training_set = tf.contrib.learn.datasets.base.load_csv_with_header(
        filename=IRIS_TRAINING,
        target_dtype=np.int,
        features_dtype=np.float32)
    test_set = tf.contrib.learn.datasets.base.load_csv_with_header(
        filename=IRIS_TEST,
        target_dtype=np.int,
        features_dtype=np.float32)

    # Specify that all features have real-value data
    feature_columns = [tf.feature_column.numeric_column("x", shape=[4])]

    
    # Define the training inputs
    train_input_fn = tf.estimator.inputs.numpy_input_fn(
        x={"x": np.array(training_set.data)},
        y=np.array(training_set.target),
        num_epochs=None,
        shuffle=True)

    # Define the test inputs
    test_input_fn = tf.estimator.inputs.numpy_input_fn(
        x={"x": np.array(test_set.data)},
        y=np.array(test_set.target),
        num_epochs=1,
        shuffle=False)

    # Classify two new flower samples.
    new_samples = np.array(
        [[6.4, 3.2, 4.5, 1.5],
         [5.8, 3.1, 5.0, 1.7]], dtype=np.float32)
    predict_input_fn = tf.estimator.inputs.numpy_input_fn(
        x={"x": new_samples},
        num_epochs=1,
        shuffle=False)

    predictions = list(classifier.predict(input_fn=predict_input_fn))
    predicted_classes = [p["classes"] for p in predictions]

    print(
        "New Samples, Class Predictions:    {}\n"
        .format(predicted_classes))


if __name__ == "__main__":
    main()
