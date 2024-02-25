# -*-coding: Utf-8 -*-
# @File : 12_爬虫_urllib_微博的cookie登陆 .py
# author: fwx
# Time：2024/1/24

import urllib.request

url = 'https://weibo.cn/5385420040/info'

# *** headers 里面主要起作用的是 Cookie， 有的网站会校验 Referer，这个参数用于做防盗链
headers = {
    # ':Authority':'weibo.cn',
    # ':Method':'GET',
    # ':Path':'/5385420040/info',
    # ':Scheme':'https',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    # 'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'zh-CN,zh;q=0.9,und;q=0.8',
    'Cookie':'WEIBOCN_WM=3349; _T_WM=ac4b4829a0639a0787af8fcba93f6d86; MLOGIN=1; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhF.q99F1bE.05Vd0WJ-nb85JpX5KzhUgL.Fo-01h-Xeo57Sh52dJLoIp7LxKML1KBLBKnLxKqL1hnLBoMfe0nfShz7ehB7; SUB=_2A25ItKOtDeRhGeNN41cV8i7MzzyIHXVry7llrDV6PUJbkdANLRajkW1NSZi25nl87uFIv2kdpk_JscZ0uYsO99hA; SCF=AvsSn0u-GbizTF_BEA4SXCWRqQtKRwH3U4IM_wzfa1YBiZH8qquxqb-l-heVQUQEqs_5et3rEUrUy53Ns_w1zxQ.; SSOLoginState=1706087421',
    'Referer':'https://weibo.cn/',
    'Sec-Ch-Ua':'"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'Sec-Ch-Ua-Mobile':'?0',
    'Sec-Ch-Ua-Platform':'"Windows"',
    'Sec-Fetch-Dest':'document',
    'Sec-Fetch-Mode':'navigate',
    'Sec-Fetch-Site':'same-origin',
    'Sec-Fetch-User':'?1',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.289 Safari/537.36',
}

request = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')

with open('../sourceFile/weibo_info.html','w',encoding='utf-8') as file:
    file.write(content)
    file.close()