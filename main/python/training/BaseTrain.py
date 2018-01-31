import main.python.utils.fileUtils
import main.resource.dataloader.DataLoaderConfig
import pdb
import os

class BaseTrain():
    # init function for 
    def __init__(self, path, time_string):
        # check path valid
        assert fileUtils.isFolderExists(path)
        self.path = path
        self.ts = time_string
        return
    
    # this is a abstract function
    def train(self):
        raise NotImplementedError()

    def evaluate(self):
        raise NotImplementedError()

    def send(self):
        return

    def writeLog(self, str):
        fn = os.path.join(self.path, self.ts + '.' + )
        return

    def submitModel(self):
        return