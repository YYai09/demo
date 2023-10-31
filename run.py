# -*-coding:utf-8-*-
# @Time    :2023/10/3014:37
# @Author  :wsy
# @Email   :2960388548@qq.com
# @File    :run.py
# @Software:PyCharm

import HTMLTestRunnerNew
from ceshi import *

suite=unittest.defaultTestLoader.discover(".",pattern="ceshi.py")
with open("reports.html","wb+") as f:
    runner=HTMLTestRunnerNew.HTMLTestRunner(f,2,title="测试报告",description="login reports",tester="yai")
    runner.run(suite)