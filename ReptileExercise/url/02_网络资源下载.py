# -*-coding: Utf-8 -*-
# @File : 02_网络资源下载 .py
# author: fwx
# Time：2024/1/16

import urllib.request
import urllib.response

# 1.网页下载
# url1='http://www.baidu.com'
# response = urllib.request.urlretrieve(url1,'../sourceFile/baidu.html')

# 2.图片下载
# url2='https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fsafe-img.xhscdn.com%2Fbw1%2Fbf774a39-4b2a-4b99-a714-87d59650a91b%3FimageView2%2F2%2Fw%2F1080%2Fformat%2Fjpg&refer=http%3A%2F%2Fsafe-img.xhscdn.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1707981713&t=98f46dbcbefc8db36d9fd7d92737e794'
# response = urllib.request.urlretrieve(url2,'../sourceFile/tmac.jpg')

# 3.视频下载
url3 = 'https://vd4.bdstatic.com/mda-pm44ywvz7k1fq9tz/sc/cae_h264/1701804740851823555/mda-pm44ywvz7k1fq9tz.mp4?v_from_s=hkapp-haokan-hbf&amp;auth_key=1705400721-0-0-9fe05664b4cf64d4e89afd19ed4cd368&amp;bcevod_channel=searchbox_feed&amp;cr=2&amp;cd=0&amp;pd=1&amp;pt=3&amp;logid=1521429486&amp;vid=940668622848726432&amp;klogid=1521429486&amp;abtest='
response = urllib.request.urlretrieve(url3,'../sourceFile/tmac.mp4')
