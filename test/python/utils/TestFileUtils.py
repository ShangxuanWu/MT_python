# CopyRight Shangxuan Wu @ Myriad of Things
# File Created in Feb 2018

# add path for root ('tf_code/') directory if not in sys.path
import sys, os
root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
if root_path not in sys.path
    sys.path.append(root_path)

from main.python.utils import FileUtils

if __name__ == "__main__":
    # test some function in FileUtils.py here
    pass