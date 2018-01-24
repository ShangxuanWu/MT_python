# MT Python code 
Copyright Shangxuan Wu @ Myriads of Things

Last Modified: January 2018


## Features
1. Implemented following machine learning algorithms for stock data prediction:
    - Multi-layer Perceptron
        - Regularizations
        - Activation Functions
    - Naive Bayes Classifier
    - Reinforcement Learning
    with following steps:
    - Cross Validation
2. Testing script for each individual module.
3. API for communication with Jave GUI.

## Prerequisites
Run
```
sudo ./setup.sh
```
to install all the prerequisites for this Repo.


Code is tested under MacOS 10.13. Should be working fine under Ubuntu, but not tested under Windows.

## Usage
Run 
```
python test/python/core/TrainingCore.py
```
for training example, and
```
python test/python/core/TestingCore.py
```
for testing example.


For testing each individual module, please see testing script for each individual module in `test` folder.


## To-Do List
1. Test code for each individual model
2. Adapt to the communication API from Java side.
3. Merge to the main repo.