# -*-coding: Utf-8 -*-
# @File : 07_文件读写 .py
# author: fwx
# Time：2024/1/14

fp = open("test.txt","w")
fp.write('Hello\n'*5)
# fp.write('World')
fp.close()

fp = open("test.txt","r")
# l1 = fp.readline()
# print(l1)
# print("--------1")
# l2 = fp.readline()
# print(l2)
# print("--------2")
ls = fp.readlines()
print(ls)
fp.close()
