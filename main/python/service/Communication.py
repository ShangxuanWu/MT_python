# CopyRight Shangxuan Wu @ Myriad of Things
# File Created in Jan 2018

# add path for root ('tf_code/') directory if not in sys.path
import sys, os
root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
if root_path not in sys.path
    sys.path.append(root_path)

import shutil, pdb, logging
from main.python.utils import FileUtils

class Communication:
    def __init__(self, root):
        self.root = root
        self.logger = logging.getLogger('COMMUNICATION')
        return

    # before training, we have to copy input files to some folder under root folder
    # @output: bool, indicates a good receive operation or not
    def receiveModel(self, src, time_string, delete_src=False):
        dst = os.path.join(self.root, time_string)
        # if the src folder does not exist
        if not FileUtils.isFolderExist(src):
            self.logger.error("The source folder %s does not exist! Receiving aborted!" % src)
            return False

        # if the destination exists:
        if FileUtils.isFolderExist(dst):
            self.logger.error("The destination folder %s exists! Receiving aborted!" % dst)
            return False

        # do 'mv' or 'cp'
        if delete_src:
            # mv
            shutil.move(src, dst)
        else:
            # cp
            shutil.copytree(src, dst)
        self.logger.info("Model received from %s" % src)
        return True
    
    # after finish training, send the model back to the server.
    # @input: time_string: folder name
    def sendModel(self, time_string, dst, delete_src=False):
        src = os.path.join(self.root, time_string)
        # if the destination exists:
        if FileUtils.isFolderExist(dst):
            self.logger.error("The destination folder %s exists! Sending aborted!" % dst)
            return False

        # do 'mv' or 'cp'
        if delete_original:
            # mv
            shutil.move(src, dst)
        else:
            # cp
            shutil.copytree(src, dst)
        self.logger.info("Model sent to %s" % dst)
        return True

    # this function is not implemented yet because we are using log file as the way to update UI component
    def sendTrainingStatus():
        raise NotImplementedError
        return

if __name__ == "__main__":
    pass

