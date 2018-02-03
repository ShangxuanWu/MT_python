# Copyright Shangxuan Wu @ Myriad of Things
# 24 Jan 2018

# functions in this file is specifically for MT, not for general file operations


# add path for root ('tf_code/') directory if not in sys.path
import sys
from os import path
root_path = path.dirname(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
if root_path not in sys.path
    sys.path.append(root_path)

import os, pdb, time, datetime, shutil
import numpy as np
from main.resource.dataloader import DataLoaderConfig
from main.python.utils import fileUtils

class DataLoader:
    # this constructor is explicitly checking for all files existing
    def __init__(self, fd_path):
        self.root_fd = fd_path
        assert hasNecessaryTrainFiles(), "Necessary file missing for training! Please check."
        self.config_path = os.path.join(fd_path, config_basename)
        self.train_data_path = os.path.join(fd_path, train_data_basename)
        self.train_label_path = os.path.join(fd_path, train_label_basename)
        self.train_data_path = os.path.join(fd_path, train_data_basename)        
        return

    # assert 4 files exist for the given path exist in the given folder
    def hasNecessaryTrainFiles(self):
        for basename in DataLoaderConfig.init_fns:
            if not fileUtils.isFileExists(os.path.join(self.root_fd, basename)):
                return False
        return True

    # assert 5 files (3 + model + log) exist for the given timestring exist in folder
    def hasFullFiles(self):
        for suffix in DataLoaderConfig.full_fns:
            if not fileUtils.isFileExists(os.path.join(self.root_fd, ts + '.' + suffix)):
                return False
        return True

    # load data header file given path, basically useless
    def loadDataHeaderFile(path):
        dataheader_path = path + full_fns[0]
        assert isFileExists(dataheader_path)
        return

    # split train data into train and validation sets
    # suppose it is 2d data
    def splitTrainData(self, data, label):
        # TODO: determine how we can 
        num = self.data.shape[0]
        portion = int(num * train_val_split_portion)
        train_data = data[:portion, :]
        train_label = label[:portion, :]
        val_data = data[portion:, :]
        val_label = label[portion:, :]
        return train_data, train_label, val_data, val_label

    def loadTrainData(self):
        data = fileUtils.loadCSVFile(self.train_data_path)
        label = fileUtils.loadCSVFile(self.train_label_path)
        # TODO: should we do rounding for data?
        train_data, train_label, eval_data, eval_label = splitTrainData(data, label)
        return data, label

    def loadTestData(self):
        data = fileUtils.loadCSVFile(self.train_data_path)        
        return data

    # load log file given path, basically useless
    def loadLogFile(self):
        raise NotImplementedError("logLogFile() is not implemented!")
        return

    # load model file given path
    def loadModelFolder(self):
        
        assert isFolderExists(modelfolder_path)
        # how to switch between different model files?

        return
    
    # use dictionary to get config file from json data
    def loadConfigFile(self):
        data = fileUtils.loadJSONFile(self.config_path)
        # do some post-processing

        return 


if __name__ == "__main__":
    pass