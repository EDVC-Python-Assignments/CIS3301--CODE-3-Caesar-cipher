import os,sys
from mock_input_tests import *

def check_if_file_exists():
    try:
        exists = os.path.exists("code_2.py")
        assert exists == True
    except:
        sys.exit()
