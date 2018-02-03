# Shangxuan Wu @ Myraid of Things
# 31 Jun 2017

# add path for root ('tf_code/') directory if not in sys.path
import sys
from os import path
root_path = path.dirname(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
if root_path not in sys.path
    sys.path.append(root_path)

from main.python.utils import fileUtils
from main.python.dataloader import DataLoader
from main.resource.dataloader import DataLoaderConfig
import pdb
import os, logging

# this is actually an abstract class with no actual use
class BaseTrain():
    # init function for 
    def __init__(self, fd_path, child_class_name):
        # check path valid
        assert fileUtils.isFolderExists(fd_path)
        self.root_fd = fd_path

        # check three necessary files exist
        self.data_loader = DataLoader(self.root_fd)
        # already checked file existence
        #assert self.data_loader.hasNecessaryTrainFiles()
        
        # create folders
        self.model_fd = os.path.join(self.root_fd, model_fd_basename)
        fileUtils.makeOrClearFolder(root_fd)

        # handle logging        
        self.train_log_fn = os.path.join(self.root_fd, train_log_basename)        
        # create logger with 'spam_application'
        self.logger = logging.getLogger(child_class_name)
        self.logger.setLevel(logging.DEBUG)
        # create file handler which logs even debug messages
        fh = logging.FileHandler(self.train_log_fn)
        fh.setLevel(logging.DEBUG)
        # create console handler with a higher log level
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        # create formatter and add it to the handlers
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        # add the handlers to the logger
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)
        
        return
    
    # following are some abstract functions
    def parseParames(self):
        raise NotImplementedError

    def train(self):
        raise NotImplementedError

    def evaluate(self):
        raise NotImplementedError

    def send(self):
        raise NotImplementedError

    def writeLog(self, str):
        fn = os.path.join(self.path, self.ts + '.')
        return

    def submitModel(self):
        return