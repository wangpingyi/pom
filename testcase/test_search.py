# -- coding:utf-8 --
"""
作者：WPY

日期：2022年 03月 01日

"""
import sys
sys.path.append('D:\pom')
from myunit import Munit
from pages.baidu_page import BaiduPage
from time import sleep

class TestCase(Munit):

    def test_suosou(self):
        bd = BaiduPage(self.driver)
        bd.suosou('全国姓谭的人数')
        sleep(3)