# -*- coding: utf-8 -*-
__author__ = 'qianqing'

import os
import unittest
import HTMLTestRunner
from time import strftime
from appium import webdriver
from ujing.ujing_element import Element

class AndroidWebViewTest(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1'
        desired_caps['deviceName'] = '23d76415'
        desired_caps['appPackage'] = 'com.midea.vm.washer'
        desired_caps['appActivity'] = 'com.midea.vm.washer.MainActivity'
        desired_caps['unicodeKeyboard'] = 'True'
        desired_caps['noSign'] = 'True' # 禁止重签名
        desired_caps['newCommandTimeout'] = 600  # 设置Appium最大等待时间，默认是60s未收到命令就关闭
        # desired_caps['autoAcceptAlerts'] = 'True' # 自动接受提示信息

        self.wd = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

        try:
            self.wd.implicitly_wait(10)
            self.wd.find_element_by_name('暂不升级').click()
        except:
            pass

    def tearDown(self):
        self.wd.quit()

    def current_time(self):
        time = os.path.join('测试时间: ' + strftime('%Y/%m/%d/%H:%M:%S'))
        print time

    def test_case01(self):
        sp = Element(self.wd)
        sp.yuyue_wash()

def suite():
    suiteTest=unittest.TestSuite()
    suiteTest.addTest(AndroidWebViewTest("test_case01"))
    return suiteTest

if __name__ == '__main__':
    now_time = strftime("%Y-%m-%d_%H:%M:%S")
    version = float(input('Please input version: '))
    version = bytes(version)
    fp = open("result_" + "v" + version + "_" + now_time + ".html", 'wb')

    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'测试报告', description=u'测试报告的描述')
    runner.run(suite())
    fp.close()