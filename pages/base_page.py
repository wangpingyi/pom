# -- coding:utf-8 --
"""
作者：WPY

日期：2022年 03月 01日

"""
class BasePage:

    def __init__(self,driver):
        self.driver = driver

    def find_element(self,*loc):

        return self.driver.find_element(*loc)

    def find_elements(self,*loc):

        return self.driver.find_elements(*loc)
