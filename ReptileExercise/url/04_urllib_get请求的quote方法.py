# -*-coding: Utf-8 -*-
# @File : 04_urllib_get请求的quote方法 .py
# author: fwx
# Time：2024/1/17

# 浏览器实际地址 https://www.baidu.com/s?wd=%E5%91%A8%E6%9D%B0%E4%BC%A6
import urllib.request
import urllib.parse
url = 'https://www.baidu.com/s?wd='
name = urllib.parse.quote("周杰伦")
url = url + name

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.289 Safari/537.36'}
# 构建请求对象
request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')

print(content)