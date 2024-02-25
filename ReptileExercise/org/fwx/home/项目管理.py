from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

# 定义浏览器,设置环境
browser = webdriver.Chrome()

# 打开家园页面并写入账号密码
browser.get( 'http://172.16.0.199/pmpt/login' )
browser.find_element( 'name', 'principal' ).send_keys( '冯文翔' )
browser.find_element( 'name', 'password' ).send_keys( "runbaomi" )

# 手动输入验证码并登录
print( '请在下面输入验证码' + '↓' ),
browser.find_element_by_xpath("//input[@value='登录']").click()
print( '已登录' )
browser.implicitly_wait( 5 )
print( '跳转到日报界面' )

# 窗口最大化
browser.maximize_window()

# 点击工时管理导航。这里直接用.click会报错
menu_a = browser.find_elements_by_xpath("//ul/li[@class='treeview']/a")[4]
browser.execute_script("arguments[0].click();", menu_a)
print("打开" + menu_a.text)
browser.implicitly_wait(5)
# 点击工时列表
submenu_a = browser.find_element_by_xpath("//ul/li/a[@data-id='205']")
browser.execute_script("arguments[0].click()",submenu_a)
browser.implicitly_wait(5)

browser.maximize_window()

# 进入到iframe中
iframe = browser.find_element("id", "iframe205")
browser.switch_to.frame(iframe)
# print(browser.page_source)
browser.implicitly_wait(5)

# 列表搜索条件
browser.find_element_by_xpath("//input[@id='userName']").send_keys("冯文翔")
time.sleep(5)
browser.find_element_by_id("searchBtn").click()
browser.implicitly_wait(5)

# 滑到网页底部
# 方式一
browser.find_element_by_tag_name( 'body' ).send_keys( Keys.END )
# 方式二
browser.execute_script('document.documentElement.scrollTop=100000')

# 获取查询结果页数，页面没有页面总数显示，直接写死116
# data = browser.find_element_by_xpath("//li[@class='next']/a")
# print("****" + data.text)
i=1
while i <= 116:
    try:
        browser.get_screenshot_as_file( f"D:/fengwenxiang/project/page_" + str( i ) + ".png" )
        print( "完成第" + str( i ) + "页截图" )
        print( "~~~~~~~~~~~~~~" )
        browser.find_element_by_xpath( "//li[@class='next']/a" ).click()
        i = i + 1
        time.sleep( 2 )
    except:
        break


# 退出
print( "截图完毕，即将退出" )
time.sleep(2)
browser.quit()
print( '结束' )
