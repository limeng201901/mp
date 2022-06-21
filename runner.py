import logging
import os
import sys

import pytest
sys.path.append(os.path.dirname(sys.modules[__name__].__file__))

if __name__=="__main__":
    logging.info("start to execute testcases")
    # cmd='cd testcase'
    # os.system(cmd)
    dir=os.path.dirname(__file__)

    pytest.main(['-sq', dir+'/testcase/test_market.py','--alluredir','allure-report'])
