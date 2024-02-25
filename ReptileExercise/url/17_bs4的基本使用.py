# -*-coding: Utf-8 -*-
# @File : 17_bs4的基本使用 .py
# author: fwx
# Time：2024/2/2

# *** 安装 ***
# pip install bs4

from bs4 import BeautifulSoup

soup = BeautifulSoup(open("../sourceFile/17_bs4的基本使用.html","r",encoding="utf-8"),"lxml")

# *** find
# 返回第一个
# a = soup.find("a")
# print(a)

# 返回title="a2“的a
# a = soup.find("a",title="a2")
# print(a)

# 返回class="a1“的a
# a = soup.find("a",class_="a1")
# print(a)

# *** findall
# all = soup.findAll("a")
# all = soup.findAll(['a','span'])
# all = soup.findAll('a',limit=2)
# print(all)

# *** select (推荐)
# 类选择器
# print(soup.select(".a1"))

# id 选择器
# print(soup.select("#l1"))

# li 标签中，有 id 属性的
# print(soup.select("li[id]"))

# li 中 id=l1 的
# print(soup.select("li[id='l1']"))

# 层级选择器
# 后代选择器，div 下的 li
# print(soup.select("div li"))

# 子代选择器
# print(soup.select("div > ul >li"))

# 所有 a li
# print(soup.select("a,li"))

# 节点内容
# obj = soup.select("#d1")[0]
# 如果还有一层标签就获取不到值
# print(obj.string)
# 推荐！！！
# print(obj.get_text())

# 获取节点属性
obj = soup.select("#p1")[0]
print(obj.attrs)
print(obj.attrs.get("class"))
print(obj.get("class"))
print(obj["class"])