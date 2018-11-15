# coding:utf-8
import unittest
import ddt
import os
import requests
from time import sleep
from excelddtdriver.common import base_api
from excelddtdriver.common import readexcel
from excelddtdriver.common import writeexcel

# 获取demo_api.xlsx路径
curpath = os.path.dirname(os.path.realpath(__file__))
testxlsx = os.path.join(curpath, "demo_api.xlsx")

# 复制demo_api.xlsx文件到report下
report_path = os.path.join(os.path.dirname(curpath), "report")
reportxlsx = os.path.join(report_path, "result.xlsx")

testdata = readexcel.ExcelUtil(testxlsx).dict_data()

@ddt.ddt
class Test_api(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("......Start......")
        cls.s = requests.session()
        # 如果有登录的话，就在这里先登录了
        writeexcel.copy_excel(testxlsx, reportxlsx) # 复制xlsx  调用writeexcel.copy_excel函数

    @classmethod
    def tearDownClass(cls):
        sleep(3)
        print("......End......")

    @ddt.data(*testdata)
    def test_api(self, data):
        # 先复制excel数据到report
        res = base_api.send_requests(self.s, data)    #调用base_api.send_requests函数

        base_api.wirte_result(res, filename=reportxlsx)   #调用base_api.wirte_result函数
        # 检查点 checkpoint
        check = data["checkpoint"]
        print("检查点->：%s"%check)
        # 返回结果
        res_text = res["text"]
        print("返回实际结果->：%s"%res_text)
        # 断言
        self.assertTrue(check in res_text)

if __name__ == "__main__":
    unittest.main()