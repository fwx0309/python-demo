# -*-coding: Utf-8 -*-
# @File : 16_解析_jsonpath .py
# author: fwx
# Time：2024/2/2

# *** 安装 ***
# pip install jsonPath -i https://pypi.doubanio.com/simple/

import json
import jsonpath

# 读取网路数据同理，抓取到数据后解析即可
# *** 加载本地文件数据。
# jsondata = json.load(open("../sourceFile/16_jsonpath.json","r",encoding="utf-8"))

# *** 加载字符串变量数据
jsonStr = '''{
  "store": {
    "book": [
      {
        "category": "修真",
        "author": "六道",
        "title": "坏蛋是怎样练成的",
        "price": 8.95
      },
      {
        "category": "修真",
        "author": "天蚕土豆",
        "title": "斗破苍穹",
        "price": 12.99
      },
      {
        "category": "修真",
        "author": "唐家三少",
        "title": "斗罗大陆",
        "isbn": "0-553-21311-3",
        "price": 8.99
      },
      {
        "category": "修真",
        "author": "南派三叔",
        "title": "星辰变",
        "isbn": "0-395-19395-8",
        "price": 22.99
      }
    ],
    "bicycle": {
      "author": "老马",
      "color": "黑色",
      "price": 19.95
    }
  }
}'''
jsondata = json.loads(jsonStr)

# store 下面的所有元素
# eles = jsonpath.jsonpath(jsondata,"$.store.*")
# print(eles)

# 所有的书
# eles = jsonpath.jsonpath(jsondata,'$..book.*')
# print(eles)

# 所有的书名
# eles = jsonpath.jsonpath(jsondata,'$.store.book[*].title')
# print(eles)

# 最后一本书的名字
# eles = jsonpath.jsonpath(jsondata,'$.store.book[(@.length-1)].title')
# print(eles)

# 包含 isbn 元素的书名
# eles = jsonpath.jsonpath(jsondata,'$..book[?(@.isbn)].title')
# print(eles)

# 前两本书的名字
# eles = jsonpath.jsonpath(jsondata,'$..book[:2].title')
eles = jsonpath.jsonpath(jsondata, '$..book[0,1].title')
print(eles)
