from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


# 定义浏览器,设置环境
# chromedriver = webdriver.Chrome("D:/Program Files/Python/Python38/chromedriver.exe")
browser = webdriver.Chrome()

# 打开家园页面并写入账号密码
browser.get( 'http://www.yjt.run.com/YJT_Admin/' )
browser.find_element( 'id', 'username' ).send_keys( '冯文翔' )
browser.find_element( 'id', 'password' ).send_keys( "!f123456789" )

# 手动输入验证码并登录
print( '请在下面输入验证码' + '↓' ),
yzm = input()
browser.find_element( 'id', 'code' ).send_keys( yzm )
browser.find_element( 'id', 'loginOkA' ).submit()
print( '已登录' )
browser.implicitly_wait( 10 )
print( '跳转到日报界面' )

# 窗口最大化
browser.maximize_window()

# 写入开始时间和结束时间并查询(!!!!!!开始时间、结束时间、用户名自行设定!!!!!!!!!)
kstime = browser.find_element( 'id', 'startDate' )
browser.execute_script( "arguments[0].value='2023-03-06';", kstime )
jstime = browser.find_element( 'id', 'endDate' )
browser.execute_script( "arguments[0].value='2024-01-30';", jstime )
user = browser.find_element( 'id', 'applyUser' )
browser.execute_script( "arguments[0].value='冯文翔';", user)
browser.find_element('id', 'selectDaily').click()
print("日报查询")

# time.sleep(2)
browser.implicitly_wait( 10 )

# 获取查询结果页数
page_str = browser.find_element_by_xpath("//span[@class='r-grid-indexPage']").text
page = page_str.strip('/页')
print("获取日报页面有"+page+"页")
print( "~~~~~~~~~~~~~~~~~~~" )

# 测试page变量是否int类型
# if isinstance(page, int):
#     print("page is int")
# else:
#     print("page is str")
page = int(page)

# 完成当前页面10条日报查看并截图后，点击下一页再进行循环
i = 1


while i <= page:
        print( "打开第" + str( i ) + "页" )
        time.sleep( 5 )
        # 定位当前页所有查看按钮元素
        chakan_lst = browser.find_elements_by_xpath( "//a[text()='查看']" )
        # 读取元素列表，依次点击按钮并截图

        for chakan in chakan_lst:
            # 点击元素
            chakan.click()
            browser.implicitly_wait( 10 )
            # 获取日报的日期
            ribao_time = browser.find_element( 'id', 'dailyDate' ).text
            print( "===打开" + ribao_time + "日报" )
            # !!!!!!!!截图并保存到指定路径!!!!!!!
            browser.get_screenshot_as_file( f"D:/fengwenxiang/new-home-ribao/" + ribao_time + "_1" + ".png" )
            print( "===完成" + ribao_time + "截图-1" )
            # 选中页面主体并点击鼠标
            browser.find_element_by_tag_name( 'body' ).click()

            # 发送按键END跳转到网页尾部，并截图
            browser.find_element_by_tag_name( 'body' ).send_keys( Keys.END )
            browser.get_screenshot_as_file( f"D:/fengwenxiang/new-home-ribao/" + ribao_time + "_2" + ".png" )
            print( "===完成" + ribao_time + "截图-2" )
            print( "~~~~~~~~~~~~~~~~~~~" )
            # 点击返回按钮退出
            browser.find_element_by_xpath( "//a[@class='r-window-button btn_close']" ).click()
        if i < page:
            browser.find_element_by_xpath( "//a[@class='r-grid-nextPage']" ).click()
            i = i + 1
        else:
            break





# 退出
print( "截图完毕，即将退出" )
time.sleep(2)
browser.quit()
print( '结束' )
