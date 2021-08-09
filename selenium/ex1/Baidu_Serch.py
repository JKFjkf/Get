# coding=utf-8
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
# from selenium.common.exceptions import
from selenium.webdriver.support.ui import WebDriverWait  # available since
from selenium.webdriver.common.keys import Keys

from time import sleep

import os, time

driver = webdriver.Chrome()
print(u"加载驱动完成..")
driver.get("https://ww.baidu.com")  # 加载页面
print(u"加载页面完成..")

time.sleep(1)

# 方法一
try:
    assert u"百度一下" in driver.title
    print('Assertion baidu title pass.')
except Exception as e:
    print('Assertion baidu title fail.', format(e))

driver.maximize_window()  # 浏览器全屏显示

print(u"最大化页面窗口完成..")

elem = driver.find_element_by_name("wd")  # Find the query box
elem.send_keys(u"今日头条" + Keys.RETURN)
elem.submit()  #提交表单方法

print(u"输入搜索关键字...")

time.sleep(1)  # Let the page load, will be added to the API

'''
#driver.find_element_by_id("kw").clear()
#driver.find_element_by_id("kw").send_keys(u"pyse自动化测试")
#driver.type("//*[@id='kw']",u"pyse自动化测试")
#driver.find_element_by_id("su").send_keys(Keys.ENTER)
#driver.click("//*[@id='su']")
#也可定位登陆按钮，通过enter（回车）代替click()
driver.find_element_by_id("su").send_keys(Keys.ENTER)
'''
# 方法一  采用包含判断,建议第一种
try:
    driver.find_element_by_xpath("//*[@id='su']")
    print("校验通过，百度一下按钮存在")
except NoSuchElementException:
    assert 0, "校验不通过"
# raw_input()#停止在当前光标处；
# 方法二
# time.sleep(1)
sleep(1)
# 验证 今日头条_百度搜索 标题是否存在
if u"今日头条_百度搜索" == driver.title:
    print('Assertion dayevenery title pass.')
else:
    print('Assertion dayevenery title fail.')

print
driver.title
# raw_input()#停止在当前光标处；
# 更多验证方法
'''
try:  
            self.assertEqual(u"今日头条_百度搜索", driver.title)

            print u"标题验证 Pass"
except AssertionError as e:  
            print u"找不到这个标题"

try:  
            assert u"今日头条_百度搜索" in driver.title
            self.assertFalse(driver.title)
            print u"标题验证 True"
except AssertionError as e:  
            print u"找不到这个标题 Flase"

#判断页面上有无id为kw的元素
if is_element_exist("#kw") :
                driver.find_element_by_id("kw").send_keys("")
#判断页面有无标签为input元素
if is_element_exist("input") :
                driver.find_element_by_tag_name("input").send_keys("eveneryday news!")
'''
# ==================================
try:
    # we have to wait for the page to refresh, the last thing that seems to be updated is the title
    WebDriverWait(driver, 10).until(lambda driver: driver.title.lower().startswith(""))

    # You should see "cheese! - Google Search"
    print
    u"等待时间，打印当前页面的标题 ：" + driver.title

finally:
    print(u"-----> 请按Enter 键进行下一步操作...")

    input()  # 停止在当前光标处；

    # driver.close()
    print(u"执行完成，即将关闭驱动...")

    driver.quit()  # 与close方法相同
    driver.quit()

    # ==================================