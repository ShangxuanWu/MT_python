# MT Python code 
Copyright Shangxuan Wu @ Myriads of Things

Last Modified: Feb 2018


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
We suppose that Java frontend would create the following three files for us:
1. 20180131_235959/data_header
2. 20180131_235959/train_data
3. 20180131_235959/train_label
4. 20180131_235959/test_data
5. 20180131_235959/config

and with the training process we would get follwing files:

6. 20180131_235959/model
7. 20180131_235959/train_log

Run
```
python AddPath.py
```
first, then:

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

## Parameter List for Different Methods
1. Multi-layer Perceptron
2. Naive Bayes
3. RNN
4. LSTM


## Format of `config` File
The `config` file is in JSON format. Please follow the following guideline for creating a `config` file.
1. 

## To-Do List
1. Test code for each individual model
2. Adapt to the communication API from Java side.
3. Merge to the main repo.