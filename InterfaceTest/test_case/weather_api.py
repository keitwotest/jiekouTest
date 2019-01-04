#coding:UTF-8
"""
--------------------------------------
   File Name：  test_weather_api
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

# 构造WeatherTest类，继承unittest.TestCase
class WeatherTest(unittest.TestCase):
    # 用例执行前的准备工作
    """天气API测试"""
    def setUp(self):
        self.url = 'http://t.weather.sojson.com/api/weather/city'

    # 定义测试shenzheng天气的方法
    def test_weather_shenzheng(self):   # 用例方法需要以test开头，便于执行顺利
        '''
        Case01-正常存在的city_code值
        '''
        data = {'city_code':'1012806011'}
        r = requests.get(self.url+'/'+data['city_code'])    # 拼接接口URL
        result = r.json()   # 将返回结果转换为json类型

        # 设置断言
        self.assertEqual(result['status'],200)  # 状态码的值是数字，非字符串
        self.assertEqual(result['message'],'Success !')
        self.assertEqual(result['cityInfo']['city'],'深圳市')
        self.assertEqual(result['cityInfo']['cityId'],'101280601')
        sleep(3)    # 控制请求的间隔时间，防止过快请求而IP受限制

    def test_weather_param_error(self):
        '''
        Case02-错误的city_code值
        '''
        data = {'city_code':'666abc'}
        r = requests.get(self.url+'/'+data['city_code'])
        result = r.json()

        self.assertEqual(result['message'],'Request resource not found.')
        self.assertEqual(result['status'],404)
        sleep(3)

    def test_weather_param_non_existent(self):
        '''
        Case03-不存在的city_code值
        '''
        data = {'city_code':'123456789'}
        r = requests.get(self.url+'/'+data['city_code'])
        result = r.json()

        self.assertEqual(result['message'],'no_city_id')
        self.assertEqual(result['status'],403)
        sleep(3)

    def test_weather_no_param(self):
        '''
        Case04-不传入任何city_code值（空）
        '''
        data = {'city_code':''}
        r = requests.get(self.url+'/'+data['city_code'])
        result = r.json()

        self.assertEqual(result['message'],'Request resource not found.')
        self.assertEqual(result['status'],404)
        sleep(3)

# 调试WeatherTest类
if __name__ == '__main__':
    unittest.main()
