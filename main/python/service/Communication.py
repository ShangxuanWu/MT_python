# CopyRight Shangxuan Wu @ Myriad of Things
# File Created in Jan 2018

# add path for root ('tf_code/') directory if not in sys.path
import sys
from os import path
root_path = path.dirname(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
if root_path not in sys.path
    sys.path.append(root_path)


import os, sys, shutil
import pdb

class Communication:
    # receive raw data from server java code
    def receiveRawData(self, path, time_string):
        return

    # After finish training, send the model back to the server.
    # 
    def sendModel(self, time_string, dst, delete_original=False):
        src = os.path.join(self.root, time_string)
        # If the destination exists:
        if 
            return

        if delete_original:
            # mv
            shutil.move(src, dst)
        else:
            # cp
            shutil.copytree()
        logging.log
        return

    # this function is not implemented yet
    def receiveModel(self):
        return

    # this function is not implemented yet because we are using pull as UI updating scheme
    def sendTrainingStatus():
        return

if __name__ == "__main__":
    pass

