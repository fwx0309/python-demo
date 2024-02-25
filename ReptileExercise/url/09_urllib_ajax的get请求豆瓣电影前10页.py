# -*-coding: Utf-8 -*-
# @File : 09_urllib_ajax的get请求豆瓣电影前10页 .py
# author: fwx
# Time：2024/1/24

# https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=20
# https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=20&limit=20

import urllib.request
import urllib.parse
import json


# 分页查询请求
def getRequest(page):
    base_url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&'
    data = {
        'start': (page - 1) * 20,
        'limit': 20
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.289 Safari/537.36'
    }

    url = base_url + urllib.parse.urlencode(data)
    # 构建请求对象
    request = urllib.request.Request(url=url, headers=headers)
    # 发送请求
    response = urllib.request.urlopen(request)
    # 读取内容并转译
    content = response.read().decode('utf-8')
    return content

def download_file(page, data):
    with open('../sourceFile/doubanPage'+ str(page) +'.json', 'w',encoding='utf-8') as fp:
        fp.write(data)
        fp.close()

if __name__ == '__main__':
    baseUrl = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&'
    startNum = 1
    endNum = 10
    for page in range(startNum, endNum + 1):
        # 发送分页请求获取数据
        content = getRequest(page)
        # 将数据存到本地
        download_file(page, content)
