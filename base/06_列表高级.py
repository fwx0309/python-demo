# -*-coding: Utf-8 -*-
# @File : 06_列表高级 .py
# author: fwx
# Time：2024/1/11

l1 = [1,2,3,4,5,6,7,8,9]
l2 = [1,2,3,4,5,6,7,8,9]
l3 = [1,2,2,3]

# 索引可以是负数，但不能越界
print(l1[-1])

# 1.*** append 在末尾添加元素
l1.append(10)
print(l1)

# 2.*** insert 在指定位置插入元素
l1.insert(1,"-1")
print(l1)

# 3.*** extend 合并两个列表
l1.extend(l2)
print(l1)

# 4.*** 切片 [起始位置：结束位置：步长] ps:不包含结束位置
print(l2[1:3])
print(l2[1:])
print(l2[:4])
print(l2[:])
print(l2[::2])

# 5.*** 通用方法
print("5.*** 通用方法")
print(l3*2)
print(l3+l3)
print(len(l3))
print(max(l3))
print(min(l3))
print(2 in l3)
print(2 not in l3)
print(l3.index(2))
print(l3.index(2,1,2))
print(l3.count(2))

