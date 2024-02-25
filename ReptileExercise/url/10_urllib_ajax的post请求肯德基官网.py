# -*-coding: Utf-8 -*-
# @File : 10_urllib_ajax的post请求肯德基官网 .py
# author: fwx
# Time：2024/1/24

import urllib.request, urllib.parse


def postRequest(page):
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
    data = {
        'cname': '武汉',
        'pid':'',
        'pageIndex': 1,
        'pageSize': 10
    }
    data = urllib.parse.urlencode(data).encode('utf-8')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.289 Safari/537.36'
    }

    request = urllib.request.Request(url, data, headers)
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content


def download(page, content):
    fp = open('../sourceFile/kfc' + str(page) + '.json', 'w', encoding='utf-8')
    fp.write(content)
    fp.close()


if __name__ == '__main__':
    startPage = int(input('请输入起始页'))
    endPage = int(input('请输入结束页'))

    for page in range(startPage,endPage+1):
        # 发送 post 请求，返回请求结果
        content = postRequest(page)
        # 保存数据到本地
        download(page,content)