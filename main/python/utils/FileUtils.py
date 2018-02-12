# CopyRight Shangxuan Wu @ Myriad of Things
# Created in Jan 2018

# add path for root ('tf_code/') directory if not in sys.path
import sys, os
root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
if root_path not in sys.path:
    sys.path.append(root_path)

import pdb, time, datetime, shutil, json
import numpy as np

def isFileExist(file_path):
    return os.path.isfile(file_path)

def isFolderExist(fd_path):
    return os.path.isdir(fd_path)

# make folder if it does not exist, otherwise clear folder
def makeOrClearFolder(fd_path):
    if isFolderExists(fd_path):
        shutil.rmtree(fd_path)
    os.makedirs(directory)
    return

# Delete the file if it exists
def deleteFileIfExist(fn):
    if isFileExist(fn):
        os.remove(fn)
        print("File %s exists. Deleted!")
    return

# get time stamp in UTC
def getTimeStamp():
    time_stamp = time.time()
    return time_stamp

def getFileExtension(full_path):
    assert isFileExists()
    filename, file_extension = os.path.splitext(full_path)
    return file_extension

# get folder name from a given path
def getFolderNameFromFolderPath(fd_path):
    assert isFolderExists(fd_path), ("Given folder path '%s' does not exist." % fd_path )
    return os.path.basename(fd_path)

# get time string using time stamp from getTimeStamp()
# format: '20180131_013256'
def getTimeString(ts):
    time_string = datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d_%H%M%S')
    return time_string

def getFileNameWithoutSuffix(path, time_str):
    return os.path.join(path, time_str)

# loading basic file format: csv separated by ','
def loadCSVFile(full_path):
    assert isFileExists(full_path), ("CSV file %s does not exist!" % full_path)
    data = np.genfromtxt(full_path, delimiter=',')
    return data

# loading basic file format: JSON
def loadJSONFile(full_path):
    assert isFileExists(full_path), ("JSON file %s does not exist!" % full_path)
    with open(full_path) as json_data:
        d = json.load(json_data)
    return d