# -*-coding: Utf-8 -*-
# @File : 01_网页获取 .py
# author: fwx
# Time：2024/1/15

url = "http://www.baidu.com"

import urllib.request

response = urllib.request.urlopen(url)

comtext = response.read().decode('utf-8')

print(comtext)
