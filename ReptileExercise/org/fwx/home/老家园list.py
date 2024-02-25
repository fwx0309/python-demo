from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

# 定义浏览器,设置环境
# chromedriver = webdriver.Chrome("D:/Program Files/Python/Python38/chromedriver.exe")
browser = webdriver.Chrome()

# 打开家园页面并写入账号密码
browser.get( 'http://www.run.com/administrator.do' )
browser.find_element( 'id', 'username' ).send_keys( '冯文翔' )
browser.find_element( 'id', 'password' ).send_keys( "!f123456789" )

# 手动输入验证码并登录
print( '请在下面输入验证码' + '↓' ),
yzm = input()
browser.find_element( 'id', 'code' ).send_keys( yzm )
browser.find_element( 'id', 'loginOkA' ).submit()
print( '已登录' )

browser.implicitly_wait( 10 )

# 跳转到日报界面
browser.get( 'http://www.run.com/daily/dailyCenter.do' )
print( '跳转到日报界面' )

# 窗口最大化
browser.maximize_window()

# 切换每页日报显示条数
browser.find_element_by_xpath("//a[text()='40']").click()

# 写入开始时间和结束时间并查询(!!!!!!时间范围自行设定!!!!!!!!!)
kstime = browser.find_element( 'id', 'startTime' )
browser.execute_script( "arguments[0].value='2023-03-06';", kstime )
jstime = browser.find_element( 'id', 'endTime' )
browser.execute_script( "arguments[0].value='2024-01-30';", jstime )
browser.find_element_by_xpath( "//a[text()='查询']" ).click()
print("日报查询")

# time.sleep(2)
browser.implicitly_wait( 10 )

# 获取查询结果页数
page = browser.find_element_by_name('totalPages').get_attribute('value')
print("获取日报页面有"+page+"页")

# 测试page变量是否int类型
# if isinstance(page, int):
#     print("page is int")
# else:
#     print("page is str")

# 将str类型转为int类型
page = int(page)

i = 1
while i <= page:
    try:
        # !!!!!!!截图保存路径自行设置!!!!!!!
        browser.get_screenshot_as_file( f"D:/fengwenxiang/old-home-main-pei/page_" + str( i ) + ".png" )
        print( "完成第" + str( i ) + "页截图" )
        print( "~~~~~~~~~~~~~~" )
        browser.find_element_by_xpath( "//a[text()='下一页>']" ).click()
        i = i + 1
        time.sleep( 3 )
    except:
        break

# 退出
print( "截图完毕，即将退出" )
time.sleep(2)
browser.quit()
print( '结束' )
