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

# 写入开始时间和结束时间并查询
kstime = browser.find_element( 'id', 'startTime' )
browser.execute_script( "arguments[0].value='2023-03-06';", kstime )
jstime = browser.find_element( 'id', 'endTime' )
browser.execute_script( "arguments[0].value='2024-01-30';", jstime )
browser.find_element_by_xpath( "//a[text()='查询']" ).click()

# time.sleep(2)
browser.implicitly_wait( 10 )

# 切换每页日报显示条数
# browser.find_element_by_xpath("//a[text()='150']").click()

# 获所查询到的所有日报编号，并切割成列表
ids = browser.find_element( 'id', 'exportId' ).get_attribute( 'value' )
ids_lst = ids.split( "," )

ids_len = len(ids_lst)

# 用于测试
# ids_len = 5

i = 0
while i < ids_len-1:
    # 使用日报编号，依次打开日报页面，并截图保存---需要写个循环
    browser.get( "http://www.run.com/daily/viewDaily.do?id=" + ids_lst[i] )

    # 获取当前日报的日期
    ribao_time = browser.find_element_by_xpath( '/html/body/form/div[1]/div/div/ul/li[1]/span[2]' ).text
    print( "打开"+ribao_time+"日报页面")

    # 判断关闭按钮元素是否可见，如不可见，则截图2次；如可见，则截图1次
    gb = browser.find_element_by_xpath( "//a[text()='关闭']" ).is_displayed()
    if gb == False:
        # 截图并保存到指定路径，按日期命名(!!!!!!!!!!路径和文件夹自行创建和指定!!!!!!!!!)
        browser.get_screenshot_as_file( f"D:/fengwenxiang/old-home-ribao-pei/" + ribao_time + "_1" + ".png" )
        print( "完成" + ribao_time + "截图-1" )

        # 选中页面主体并点击鼠标
        browser.find_element_by_tag_name( 'body' ).click()

        # 发送按键END跳转到网页尾部，并截图
        browser.find_element_by_tag_name( 'body' ).send_keys( Keys.END )
        browser.get_screenshot_as_file( f"D:/fengwenxiang/old-home-ribao/" + ribao_time + "_2" + ".png" )
        print( "完成" + ribao_time + "截图-2" )
        print( "~~~~~~~~~~~~~~~~~~~" )
    else:
        browser.get_screenshot_as_file( f"D:/fengwenxiang/old-home-ribao/" + ribao_time + ".png" )
        print( "完成" + ribao_time + "截图" )
        print( "~~~~~~~~~~~~~~~~~~~" )

    # 变量加1
    i = i+1

# 退出
print( "截图完毕，即将退出" )
time.sleep(2)
browser.quit()
print( '结束' )
