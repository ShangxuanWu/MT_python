# Shangxuan Wu @ Myraid of Things
# 1 Feb 2017

# add path for root ('tf_code/') directory
import sys, pdb
from os import path
sys.path.append(path.dirname(path.dirname(path.dirname(path.dirname(path.abspath(__file__))))))
from main.python.utils import fileUtils
from main.python.dataloader import DataLoader
from main.resource.dataloader import DataLoaderConfig

class BaseTest():
    def __init__(self, path):
        return

    def loadModel(self):
        raise NotImplementedError()

    def forward(self):
        return result