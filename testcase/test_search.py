# -- coding:utf-8 --
"""
作者：WPY

日期：2022年 03月 01日

"""
import sys
import unittest
from BeautifulReport import BeautifulReport
import datetime

sys.path.append('D:\pom')
from myunit import Munit
from pages.baidu_page import BaiduPage
from time import sleep


filename = '自动化测试报告'+datetime.datetime.now().strftime('%Y_%m%d_%H%M%S')

class TestCase(Munit):

    def test_suosou(self):
        bd = BaiduPage(self.driver)
        bd.suosou('全国姓谭的人数')
        sleep(3)


if __name__ == '__main__':
    tc = unittest.defaultTestLoader.loadTestsFromTestCase(TestCase)
    suit = unittest.TestSuite(tc)
    BeautifulReport(suit).report(description='自动化测试报告',filename=filename,report_dir='./report')