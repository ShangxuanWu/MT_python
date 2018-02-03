# CopyRight Shangxuan Wu @ Myriad of Things
# 2 Feb 2018

# add path for root ('tf_code/') directory if not in sys.path
import sys
from os import path
root_path = path.dirname(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
if root_path not in sys.path
    sys.path.append(root_path)

import main.python.dataloader.DataLoader
import pdb

if __name__ == "__main__":
    pass