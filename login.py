#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
import re
import HTMLTestRunner
import time
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://manage.haizol.com/manageuser/loginform")

    def tearDown(self):
        self.driver.close()
    def test_01(self):
        self.driver.find_element_by_id("userName").send_keys("annieren@haizol.com")
        self.driver.find_element_by_id("password").send_keys("123456")
        self.driver.find_element_by_css_selector("button[type='submit']").click()
        time.sleep(3)
        current_url = self.driver.current_url
        print current_url
        if re.match("https://manage.haizol.com", current_url):
            print ("成功")
            assert True
        else:
            assert False

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(Login("test_01"))
    now = time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime(time.time()))
    fp = open(r'C:\Users\annieren\PycharmProjects\test\report\result\result.html', 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='测试报告', description=u'用例执行情况:')
    runner.run(suite)