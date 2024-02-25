# -*-coding: Utf-8 -*-
# @File : 23_requests_post请求 .py
# author: fwx
# Time：2024/2/18
import json

import requests

url = 'https://fanyi.baidu.com/sug'

data = {
    'kw': 'spider'
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.289 Safari/537.36'
}

response = requests.post(url, data=data, headers=headers)

obj = json.loads(response.text)
print(obj)