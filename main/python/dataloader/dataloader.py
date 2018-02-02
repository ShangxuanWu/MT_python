# Copyright Shangxuan Wu @ Myriad of Things
# Last Modified: 24 Jan 2018

from main.resource.dataloader import DataLoaderConfig
from main.python.utils import fileUtils

class DataLoader:
    # assert 3 files exists for the given timestring exist in the given folder  
    
    #
    def __init__(self, fd_path):
        self.root_fd = fd_path
        return
       
    def checkMTInitFilesValid(self, fd, ts):
        for suffix in DataLoaderConfig.init_fns:
            if not fileUtils.isFileExists(os.path.join(fd, ts + '.' + suffix)):
                return False
        return True

    # assert 5 files (3 + model + log) exist for the given timestring exist in folder
    def checkMTFullFilesValid(self, fd, ts):
        for suffix in DataLoaderConfig.full_fns:
            if not fileUtils.isFileExists(os.path.join(fd, ts + '.' + suffix)):
                return False
        return True

    def loadData(fd):
        assert checkFolderValid(fd)

        return

    def loadJSONData(fd):
        return



if __name__ == "__main__":
    pass