# -*-coding: Utf-8 -*-
# @File : 22_requests_get请求 .py
# author: fwx
# Time：2024/2/18

# *** 安装 ***
# pip install requests -i https://pypi.doubanio.com/simple/

# !!!!!! 测试没有通过获取不到数据
import requests

head = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
}
# 处理url携带的参数，将其封装到字典中，对应的是requests.get函数中第二个params参数
param = {'wd': '北京'}
url = 'http://www.baidu.com/s'  # 1.指定url
response = requests.get(url=url, params=param, headers=head)  # 2.发起请求
page_text = response.text  # 3.获取响应数据
print(page_text)