# -*-coding: Utf-8 -*-
# @File : 14_urllib_代理 .py
# author: fwx
# Time：2024/2/1
import random
import urllib.request

url = 'https://www.so.com/s?q=ip'
# url = 'http://www.baidu.com/s?wd=ip'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.289 Safari/537.36'
}

request = urllib.request.Request(url, headers=headers)

# 随机获取代理ip
proxies_pool = [
    {'http':'123.169.34.244:9999'},
    {'http':'60.205.132.71:80'},
]
proxies = random.choice(proxies_pool)

handler = urllib.request.ProxyHandler(proxies=proxies)
opener = urllib.request.build_opener(handler)
response = opener.open(request)

content = response.read().decode('utf-8')

with open('../sourceFile/ip.html','w',encoding='utf-8') as fp:
    fp.write(content)
