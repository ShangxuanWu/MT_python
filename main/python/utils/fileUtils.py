# CopyRight Shangxuan Wu @ Myriad of Things
# Created in Jan 2018

# add path for root ('tf_code/') directory if not in sys.path
import sys
from os import path
root_path = path.dirname(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
if root_path not in sys.path
    sys.path.append(root_path)

import os, pdb, time, datetime
import numpy as np
import main.resource.dataloader.DataLoaderConfig

def isFileExists(file_path):
    return os.path.isfile(file_path)

def isFolderExists(fd_path):
    return os.path.isdir(fd_path)

# get time stamp in UTC
def getTimeStamp():
    time_stamp = time.time()
    return time_stamp

def getFileExt(full_path):
    assert isFileExists()
    filename, file_extension = os.path.splitext(full_path)
    return file_extension

# get time string using time stamp from getTimeStamp()
# format: '20180131_013256'
def getTimeString(ts):
    time_string = datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d_%H%M%S')
    return time_string

def getFileNameWithoutSuffix(path, time_str):
    return os.path.join(path, time_str)

# load data header file given path, basically useless
def loadDataHeaderFile(path):
    dataheader_path = path + full_fns[0]
    assert isFileExists(dataheader_path)
    return

# load data file given path
def loadDataFile(path):
    data = np.genfromtxt(path + full_fns[], delimiter=',')
    return

# load log file given path
def loadLogFile(path):
    return

# load model file given path
def loadModelFolder(path):
    
    assert isFolderExists(modelfolder_path)
    # how to switch between different model files?

    return

def loadConfigFile(path):
    return 

def 