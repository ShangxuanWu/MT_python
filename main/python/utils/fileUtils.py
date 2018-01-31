# CopyRight Shangxuan Wu @ Myriad of Things
# Created in Jan 2018

import os, pdb, time, datetime

def isFileExists(file_path):
    return os.path.isfile(file_path)

def isFolderExists(fd_path):
    return os.path.isdir(fd_path)

# get time stamp in UTC
def getTimeStamp():
    time_stamp = time.time()
    return time_stamp

# get time string using time stamp from getTimeStamp()
# format: '20180131_013256'
def getTimeString(ts):
    time_string = datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d_%H%M%S')
    return time_string