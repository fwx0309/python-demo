# -*-coding: Utf-8 -*-
# @File : 24_requests_代理 .py
# author: fwx
# Time：2024/2/19

import requests

url = 'https://www.so.com/s?q=ip'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.289 Safari/537.36'
}

data = {
    'q':'ip'
}

proxie = {
    'http':'123.169.34.244:9999'
}

response = requests.get(url = url, params=data, headers=headers,proxies=proxie)

with open("../sourceFile/requestDaili.html","w",encoding="utf-8") as f:
    f.write(response.text)