# -*-coding: Utf-8 -*-
# @File : 11_爬虫_urllib_异常 .py
# author: fwx
# Time：2024/1/24
import urllib.request, urllib.error

# 正常的url
# url = 'https://blog.csdn.net/m0_58731306/article/details/132583538'

# 路径错误的url
# url = 'https://blog.csdn.net/m0_58731306/article/details/1325835381111111'

# 路径错误的url
url = 'https://blog111.csdn.net/m0_58731306/article/details/132583538'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.289 Safari/537.36'
}

# *** 报错必须写到具体类型
try:
    request = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    print(content)
except urllib.error.HTTPError:
    print('path error')
except urllib.error.URLError:
    print('domain name error')