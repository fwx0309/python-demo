# -*-coding: Utf-8 -*-
# @File : 15_解析_xpath的基本使用 .py
# author: fwx
# Time：2024/2/1

# chrome 浏览器插件
# 安装：xpath.zip解压后，直接拖到 chrome 浏览器的扩展插件中，重启浏览器。快捷键：Ctrl+Shift+x

# *** 安装 ***
# pip install lxml -i https://pypi.doubanio.com/simple/

from lxml import etree

# 本地HTML解析
tree = etree.parse("../sourceFile/15_xpath的基本使用.html")

print(tree)

# 1.//匹配所以层级    2./匹配下一层
# li_list = tree.xpath("//ul/li[@id='l1']/text()")
# li_list = tree.xpath("//ul/li/text()")
# li_list = tree.xpath("//ul/li[contains(@id,'l')]/text()")
li_list = tree.xpath("//ul/li[@class='c1']/text()")
print(li_list)
print(len(li_list))

# ****** 网络 html 解析
import urllib.request

url = "http://www.baidu.com"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.289 Safari/537.36'
}

request = urllib.request.Request(url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

tree = etree.HTML(content)

input = tree.xpath("//input[@id='su']/@value")[0]

print(input)