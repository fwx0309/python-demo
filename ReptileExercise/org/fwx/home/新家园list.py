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

# 写入开始时间和结束时间并查询(!!!!!!时间范围自行设定!!!!!!!!!)
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

# 切换每页日报显示条数
# browser.find_element_by_xpath("//a[text()='150']").click()


# 获取查询结果页数
page = browser.find_element_by_xpath("//a[@class='r-grid-numberLastPage r-grid-num']").text
print("获取日报页面有"+page+"页")

# 测试page变量是否int类型
# if isinstance(page, int):
#     print("page is int")
# else:
#     print("page is str")
page = int(page)

i = 1
while i <= page:
    try:
        browser.get_screenshot_as_file( f"D:/fengwenxiang/new-home-main/page_" + str( i ) + ".png" )
        print( "完成第" + str( i ) + "页截图" )
        print( "~~~~~~~~~~~~~~" )
        browser.find_element_by_xpath( "//a[@class='r-grid-nextPage']" ).click()
        i = i + 1
        time.sleep( 2 )
    except:
        break


'''
if nex == False:
    # 截图并保存到指定路径，按日期命名(!!!!!!!!!!路径和文件夹自行创建和指定!!!!!!!!!)
    browser.get_screenshot_as_file( f"D:/Users/panfeng/Desktop/jietu/page_1.png" )
    print( "完成page截图-1")

    # 选中页面主体并点击鼠标
    browser.find_element_by_tag_name('body').click()

    # 发送按键END跳转到网页尾部，并截图
    browser.find_element_by_tag_name('body').send_keys(Keys.END)
    browser.get_screenshot_as_file( f"D:/Users/panfeng/Desktop/jietu/page_2.png" )
    print( "完成page截图-2")
else:
    browser.get_screenshot_as_file( f"D:/Users/panfeng/Desktop/jietu/page.png" )
    print( "完成page截图" )
'''

# 切换每页日报显示条数
# browser.find_element_by_xpath("//a[text()='150']").click()

'''
# 获所查询到的所有日报编号，并切割成列表
ids = browser.find_element( 'id', 'exportId' ).get_attribute( 'value' )
ids_lst = ids.split( "," )

# 使用日报编号，依次打开日报页面，并截图保存---!!!!!!!!需要写个循环,修增加ids_list[i]变量!!!!!!!!!
browser.get( "http://www.run.com/daily/viewDaily.do?id=" + ids_lst[5] )

# 获取当前日报的日期
ribao_time = browser.find_element_by_xpath( '/html/body/form/div[1]/div/div/ul/li[1]/span[2]' ).text
print( "打开"+ribao_time+"日报页面")

#判断关闭按钮元素是否可见，如不可见，则截图2次；如可见，则截图1次
gb = browser.find_element_by_xpath( "//a[text()='关闭']" ).is_displayed()
print(gb)
if gb == False:
    # 截图并保存到指定路径，按日期命名(!!!!!!!!!!路径和文件夹自行创建和指定!!!!!!!!!)
    browser.get_screenshot_as_file( f"D:/Users/panfeng/Desktop/jietu/"+ribao_time+"_1"+".png" )
    print( "完成"+ribao_time+"截图-1")

    # 选中页面主体并点击鼠标
    browser.find_element_by_tag_name('body').click()

    # 发送按键END跳转到网页尾部，并截图
    browser.find_element_by_tag_name('body').send_keys(Keys.END)
    browser.get_screenshot_as_file( f"D:/Users/panfeng/Desktop/jietu/"+ribao_time+"_2"+".png" )
    print( "完成"+ribao_time+"截图-2")
else:
    browser.get_screenshot_as_file( f"D:/Users/panfeng/Desktop/jietu/"+ribao_time+".png" )
    print( "完成" + ribao_time + "截图" )
'''

# 退出
print( "截图完毕，即将退出" )
time.sleep(2)
browser.quit()
print( '结束' )
