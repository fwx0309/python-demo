# -*-coding: Utf-8 -*-
# @File : 02_数据类型 .py
# author: fwx
# Time：2024/1/9
# 1.类型的定义
# 2.类型判断：type()
# 3.类型转换
#   int(x) 将x转换为一个整数
#   float(x) 将x转换为一个浮点数
#   str(x) 将对象 x 转换为字符串
#   bool(x) 将对象x转换成为布尔值

# python3中 主要用int float
# *** Numbers(数字)：int long float complex(复数)
# *** int 没有长度限制
i1 = 100
print(i1)
i2 = 123_456_789
print(i2)
# 查看变类型
print(type(i1))

# d = 0123 10进制的数字不能以0开头
# 其他进制的整数，只要是数字打印时一定是以十进制的形式显示的
# 二进制 0b开头
c = 0b10 # 二进制的10
# 八进制 0o开头
c = 0o10
# 十六进制 0x开头
c = 0x10


# *** float
f1 = 1.1
print(f1)

# *** boolean(布尔类型)
b1 = True
b2 = False

# *** String（字符串）
s1 = 's1'
s2 = "s2"

# *** List（列表）
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l2 = ['a', 'b', 'c']

# *** Tuple（元组）
t1 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(t1)
print(type(t1))

# *** dictionary（字典）: {"key1":"value1","key2":"value2"}
d1 = {"name": "John", "age": 18}
