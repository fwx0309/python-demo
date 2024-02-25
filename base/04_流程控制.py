# -*-coding: Utf-8 -*-
# @File : 04_流程控制 .py
# author: fwx
# Time：2024/1/11

# 1.*** if
# 注意：代码的缩进为一个tab键，或者4个空格
"""
age = int(input("请输入你的年龄："))
if 18 <= age <= 150:
    print("已成年")
elif 18 > age >= 0:
    print("未成年")
else:
    print("输入的年龄有误")
"""

# 2.*** for
'''
str = "hello world"
for s in str:
    print(s)

l1 = [1, 2, 3, 4]
# range(开始值，结束值，步长)
for i in range(2, len(l1), 2):
    print(i)
'''

# 3.*** while 循环
'''
a = 0
while a < 10 :
    print(a)
    a += 1
else:
    print('循环结束')
'''

# 4.*** break 和 continue。 如果是多层循环，作用于最近的层的循环
a = 0
while a < 5:
    if a == 2:
        # break
        a += 1
        continue
    print(a)
    a += 1
else:
    print('循环结束')