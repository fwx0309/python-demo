# -*-coding: Utf-8 -*-
# @File : 18_selenium_基本使用 .py
# author: fwx
# Time：2024/2/4

# 1.下载谷歌浏览器驱动：http://chromedriver.storage.googleapis.com/index.html
# 2.安装selenium：pip install selenium

from selenium import webdriver

# 浏览器驱动加载
# 方式一
# path = 'chromedriver.exe'
# browser = webdriver.Chrome(path)

# 方式二：将 chromedriver.exe 放到 python 的安装目录，如：D:\2-develop\Python\Python36，
browser = webdriver.Chrome()

browser.get(url="http://www.jd.com")

print(browser.page_source)

