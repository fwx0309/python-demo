# -*-coding: Utf-8 -*-
# @File : 19_selenium_元素定位 .py
# author: fwx
# Time：2024/2/4

from selenium import webdriver

browser = webdriver.Chrome()

browser.get(url='http://www.baidu.com')

# id 定位
# print(browser.find_element_by_id('su'))

# xpath 定位
# print(browser.find_element_by_xpath("//input[@id='su']"))

# css 选择器，bs4 定位
# print(browser.find_element_by_css_selector("#su"))

# 标签属性值定位
# print(browser.find_element_by_name("wd"))

# 标签名定位
# print(browser.find_elements_by_tag_name("input"))

# link 定位
print(browser.find_element_by_link_text("图片"))


