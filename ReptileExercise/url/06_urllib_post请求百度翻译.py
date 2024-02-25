# -*-coding: Utf-8 -*-
# @File : 06_urllib_post请求百度翻译 .py
# author: fwx
# Time：2024/1/17

import urllib.request
import urllib.parse
import json

url = 'https://fanyi.baidu.com/sug'

data = {
    'kw': 'spider'
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.289 Safari/537.36'
}
# 数据在转完 Unicode 编码后，还需要使用 encode 转成 bypts
data = urllib.parse.urlencode(data).encode('utf-8')

request = urllib.request.Request(url=url, data=data, headers=headers)

response = urllib.request.urlopen(request)

result = response.read().decode('utf-8')
print(result)
# 将 json 字符串转成 json对象，会将数据里面的 Unicode 编码转成中文
json_result = json.loads(result)
print(json_result)
