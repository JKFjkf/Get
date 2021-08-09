#!C:/Python27
# coding=utf-8
from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support.wait import WebDriverWait#WebDriverWait 导入
from selenium.webdriver.common.keys import Keys
import os, time

driver = webdriver.Chrome()

driver.get(
    "https://cas.sf-express.com/cas/login?service=http%3A%2F%2Fhos.sf-express.com%2Fframe.pvt&apptiket=dbe979f1b41f6ea23622b639ceb7acac18cf829000ed010c")

time.sleep(1)

driver.maximize_window()  # 浏览器全屏显示
print('浏览器全屏显示 ...')
# 输入用户名和密码
driver.find_element_by_id("username").send_keys("89003422")

driver.find_element_by_id("password").send_keys("518.com.12")
time.sleep(10)
# 手动输入验证码
# driver.find_element_by_id("verifyCode").send_keys("ABCD")
# 点击登录
driver.find_element_by_xpath("//*[@id='loginForm']/div[5]/div/img").click()

time.sleep(8)

# 开始执行点击事件
# driver.find_element_by_id("outputButton").click()
print

print('开始执行任务,执行间隔时间为10分钟 ...')
print
for i in range(1, 3):
    ISOTIMEFORMAT = "%Y-%m-%d %X"
    strTime = time.strftime(ISOTIMEFORMAT, time.localtime())
    print
    u"正在执行第 ", i, "次...", strTime
    time.sleep(5)
    # 执行点击事件
    driver.find_element_by_id("outputButton").click()
    time.sleep(60)
    # 刷新浏览器
    driver.refresh()
    time.sleep(535)
    print
    print
    u"已执行完第 ", i, u"次，", "共延时", i * 10, "分"
    print
print('已执行完成...At The End OF,' + strTime)

print
print('开始执行方法二 ...')
print


def ClickStart():
    for i in range(1, 60):
        print
        u'正在执行第 ', i, "次 ...", strTime
        # 刷新浏览器
        time.sleep(10)
        driver.refresh()
        # 执行点击事件
        # driver.find_element_by_id("outputButton").click()
        time.sleep(590)
        print
        print
        u"已执行完第 ", i, "次", "共延时", i * 600 / 60, "分"
        print


ClickStart()
print

print('开始工作啦...')
# driver.find_element_by_id("inputButton").click()
print
print('工作已完成...')