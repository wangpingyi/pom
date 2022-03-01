# -- coding:utf-8 --
"""
作者：WPY

日期：2022年 03月 01日

"""
import time

from pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException

class BaiduPage(BasePage):

    search_box = ('id','kw')
    search_botton = ('id','su')
    baidu_msg = ('id','s-top-left')

    def suosou(self,ss):
        time.sleep(1)
        self.find_element(*self.search_box).send_keys(ss)
        self.find_element(*self.search_botton).click()
        return True

    def check_msg(self):
        try:
            str_msg = self.find_element(*self.baidu_msg).text
        except NoSuchElementException:
            print("======search failed=======")
            return False
        else:
            if '新闻' in str_msg:
                print('====search success======')
                return True
            else:
                print('======search failed=====')
                return False



