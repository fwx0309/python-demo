# -*-coding: Utf-8 -*-
# @File : 25_requests_cookie登陆古诗文网 .py
# author: fwx
# Time：2024/2/19

import requests
from bs4 import BeautifulSoup
# 1.获取页面隐藏参数：__VIEWSTATE、__VIEWSTATEGENERATOR
login_html_url = "https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx"
response_html = requests.get(login_html_url)

soup = BeautifulSoup(response_html.text,"lxml")
view_state = soup.select("#__VIEWSTATE")[0].get("value")
print("view_state: %s"%view_state)

view_state_generator = soup.select("#__VIEWSTATEGENERATOR")[0].get("value")
print("view_state_generator: %s"%view_state_generator)

# 2.验证码获取图片。
# ！这里不能使用 urllib3 中的 urlretrieve 来下载验证码图片，因为用 urlretrieve 来发送请求和后面的登录请求为两次会话，导致登录失败。
rand_code_obj = soup.select("#imgCode")[0].get("src")
print("rand_code: %s" % rand_code_obj)
session = requests.Session()
rand_code_data = session.get("https://so.gushiwen.cn" + rand_code_obj)
with open("../sourceFile/RandImg.jpg","wb") as fp:
    fp.write(rand_code_data.content)

# 3.根据验证码图片，输入验证码
rand_code = input("请输入验证码！\n")

# 4.登录请求
login_url = "https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx"

data = {
    '__VIEWSTATE': view_state,
    '__VIEWSTATEGENERATOR': view_state_generator,
    'from': 'http://so.gushiwen.cn/user/collect.aspx',
    'email': '345025106@qq.com',
    'pwd': 'fwx0203',
    'code': rand_code,
    'denglu': '登录'
}

response = session.post(url=login_url, data=data)

with open("../sourceFile/gsc_info.html","w",encoding="utf-8") as fp:
    fp.write(response.text)