# Copyright Shangxuan Wu @ Myriad of Things
# Last Modified: 24 Jan 2018

from main.python.dataloader import DataLoaderConfig
from main.python.utils import fileUtils

def checkFolderValid(fd):
    # assert 3 files exists in the given folder
    for fn in DataLoaderConfig.fns:
        if not fileUtils.isFileExists(os.path.join(fd, fn)):
            return False
    return True

def loadData(fd):
    assert checkFolderValid(fd)

    return



if __name__ == "__main__":
    pass