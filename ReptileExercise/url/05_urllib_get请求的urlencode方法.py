# -*-coding: Utf-8 -*-
# @File : 05_urllib_get请求的urlencode方法 .py
# author: fwx
# Time：2024/1/17

import urllib.request, urllib.parse

base_url = "https://www.baidu.com/s?"

data = {
    'wd':'周杰伦',
    'sex':'男',
    'location':'中国台湾'
}

data_url = urllib.parse.urlencode(data)
# 将请求数据中的中文转换为 unicode 编码
url = base_url + data_url

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.289 Safari/537.36'
}
# 构建请求对象
request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

print(content)

