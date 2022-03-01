# -- coding:utf-8 --
"""
作者：WPY

日期：2022年 03月 01日

"""
import unittest
from selenium import webdriver

class Munit(unittest.TestCase):

    def setUp(self) -> None:
        self.driver =webdriver.Chrome()
        url='http://www.baidu.com'
        self.driver.get(url)

    def tearDown(self) -> None:
        self.driver.quit()
