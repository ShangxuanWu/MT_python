# CopyRight Shangxuan Wu @ Myriad of Things
# 2 Feb 2018

# add path for root ('tf_code/') directory if not in sys.path
import sys, os
root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
if root_path not in sys.path
    sys.path.append(root_path)

import main.python.dataloader.DataLoader
from main.python.service import Communication
import pdb

if __name__ == "__main__":
    # variables
    src_path = "test/resource/"
    root = ""
    fake_time_string = ""
    dst_path = ""

    # new a instance of Communication
    com = Communication(root)
    com.receiveModel(src_path, fake_time_string)
    com.sendModel(fake_time_string, dst_path)
    pass