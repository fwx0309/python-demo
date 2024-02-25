# -*-coding: Utf-8 -*-
# @File : 21_requests_基本使用 .py
# author: fwx
# Time：2024/2/18

import requests

r = requests.get('http://www.baidu.com')


# 一个对象化和六个类型
print(type(r))

# 编码设置
r.encoding = "utf-8"

print(r.status_code)
print(r.encoding)
# print(r.text)
# print(r.content)
print(r.url)
print(r.headers)