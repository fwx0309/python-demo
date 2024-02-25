# -*-coding: Utf-8 -*-
# @File : 08_urllib_ajax的get请求豆瓣电影第一页 .py
# author: fwx
# Time：2024/1/22
import urllib.request

url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=20'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.289 Safari/537.36'
}

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

print(content)

# 写出方式一
# fp = open('../sourceFile/douban.json','w',encoding='utf-8')
# fp.write(content)
# fp.close()

# 写出方式二
with open('../sourceFile/douban1.json','w',encoding='utf-8') as fp:
    fp.write(content)
    fp.close()