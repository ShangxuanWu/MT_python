# CopyRight Shangxuan Wu @ Myriad of Things
# 1 Feb 2018
# functions in this file is specifically for 

# add path for root ('tf_code/') directory if not in sys.path
import sys
from os import path
root_path = path.dirname(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
if root_path not in sys.path
    sys.path.append(root_path)

import os, pdb, time, datetime, shutil
import numpy as np
import fileUtils
import main.resource.dataloader.DataLoaderConfig

# load data header file given path, basically useless
def loadDataHeaderFile(path):
    dataheader_path = path + full_fns[0]
    assert isFileExists(dataheader_path)
    return

# load data file given path, separated by ','
def loadDataFile(full_fn):
    assert 
    data = np.genfromtxt(full_fn, delimiter=',')
    # TODO: should we do rounding for data?
    return data

# load log file given path, basically useless
def loadLogFile(path):
    raise NotImplementedError("logLogFile() is not implemented!")
    return

# load model file given path
def loadModelFolder(path):
    
    assert isFolderExists(modelfolder_path)
    # how to switch between different model files?

    return

def loadConfigFile(path):
    return 

def 