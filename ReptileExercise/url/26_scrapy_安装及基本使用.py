# -*-coding: Utf-8 -*-
# @File : 26_scrapy_安装及基本使用 .py
# author: fwx
# Time：2024/2/19

# !!! ps:2024年2月19日，Python 3.7.0rc1，pip install scrapy -i https://pypi.doubanio.com/simple，一次性安装成功，没有遇到下面报错问题
# （1） pip install scrapy -i https://pypi.doubanio.com/simple
# (2) 报错1： building 'twisted.test.raiser' extension
#              error: Microsoft Visual C++ 14.0 is required. Get it with "Microsoft Visual C++
#              Build Tools": http://landinghub.visualstudio.com/visual-cpp-build-tools
#     解决1
#       http://www.lfd.uci.edu/~gohlke/pythonlibs/#twisted
#       Twisted‑20.3.0‑cp37‑cp37m‑win_amd64.whl
#       cp是你的python版本
#       amd是你的操作系统的版本
#       下载完成之后 使用pip install twisted的路径  安装
#       切记安装完twisted 再次安装scrapy

# （3） 报错2  提示python -m pip install --upgrade pip
#      解决2   运行python -m pip install --upgrade pip

# （4） 报错3   win32的错误
#      解决3   pip install pypiwin32

# （5） anaconda
