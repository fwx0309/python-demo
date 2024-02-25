# -*-coding: Utf-8 -*-
# @File : 03_urllib_请求对象定制 .py
# author: fwx
# Time：2024/1/16

import urllib.request

url = 'https://www.baidu.com/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.289 Safari/537.36'}
# 构建请求对象
request = urllib.request.Request(url=url, headers=headers)
# 发送请求，获取请求结果
response = urllib.request.urlopen(request)
# 获取解码后的网页内容
content = response.read().decode('utf-8')

print(content)