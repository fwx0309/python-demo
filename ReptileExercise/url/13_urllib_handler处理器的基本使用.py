# -*-coding: Utf-8 -*-
# @File : 13_urllib_handler处理器的基本使用 .py
# author: fwx
# Time：2024/2/1
import urllib.request

url = "https://www.baidu.com"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.289 Safari/537.36'
}

request = urllib.request.Request(url=url, headers=headers)

# handler 使用
handler = urllib.request.HTTPHandler
opener = urllib.request.build_opener(handler)
response = opener.open(request)

content = response.read().decode("utf-8")

print(content)
