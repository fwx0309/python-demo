# -*-coding: Utf-8 -*-
# @File : 20_selenium_handless .py
# author: fwx
# Time：2024/2/18

# 无界面浏览器。在本地测试的时候好像有问题，还是会打开本地的浏览器
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def share_browser(driver_path,url):
    chrome_options = Options()
    chrome_options.add_argument('‐‐headless')
    chrome_options.add_argument('‐‐disable‐gpu')
    path = r''+driver_path+''
    chrome_options.binary_location = path
    browser = webdriver.Chrome(chrome_options=chrome_options)
    browser.get(url)
    return browser


browser = share_browser("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",'https://www.baidu.com')
print(browser.find_element_by_id('su'))

