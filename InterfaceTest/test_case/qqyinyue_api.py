#coding:UTF-8
"""
--------------------------------------
   File Name：  test_qqkongjian_api
   Description :
   Author :    admin
   Date：     2019/1/2
   E-mail: 3227456102@qq.com
   adb_activity_package：adb shell dumpsys window w |findstr \/ |findstr name=
--------------------------------------
"""

import unittest
import requests
from time import sleep

# 构造QqyinyueTest类，继承unittest.TestCase
class QqkongjianTest(unittest.TestCase):
    # 用例执行前的准备工作
    """QQ音乐API测试"""
    def setUp(self):
        self.url = 'https://www.sojson.com/api/qqmusic'


    # 定义测试QQ音乐的方法
    def test_qq(self):   # 用例方法需要以test开头，便于执行顺利
        '''
        Case01-正常存在的qq_code值
        '''
        data = {'city_code':'984701108'}
        r = requests.get(self.url+'/'+data['city_code'])   # 拼接接口URL
        result = r.json()   # 将返回结果转换为json类型
        print(result)

        # 设置断言
        self.assertEqual(result['code'], '40310011')
        sleep(3)    # 控制请求的间隔时间，防止过快请求而IP受限制


# 调试QqkongjianTest类
if __name__ == '__main__':
    unittest.main()
