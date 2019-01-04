#coding:UTF-8
"""
--------------------------------------
   File Name：  runtest
   Description :
   Author :    admin
   Date：     2019/1/2
   E-mail: 3227456102@qq.com
   adb_activity_package：adb shell dumpsys window w |findstr \/ |findstr name=
--------------------------------------
"""

import unittest
import HTMLTestRunner_cn
from common.send_email import sendreport
import time

# 指定测试用例 & 测试报告的存放路径
testcase_dir = 'D:/work/Selenium-Demo/InterfaceTest/test_case'
report_dir = 'D:/work/Selenium-Demo/InterfaceTest/test_report'

# 加载测试用例
discover = unittest.defaultTestLoader.discover(testcase_dir,pattern='*.py')

# 定义测试报告的文件格式
now = time.strftime("%y-%m-%d %H_%M_%S")    # 对时间格式化
report_name = report_dir+'/'+now+'_test_report.html'    # 报告的名称规则

# 运行测试用例，并生成测试报告
with open(report_name,'wb') as f:
    runner = HTMLTestRunner_cn.HTMLTestRunner(stream=f,title="Interface API Test Report",description="Test Report")
    runner.run(discover)
    #发送测试报告邮件
    #sendreport()


