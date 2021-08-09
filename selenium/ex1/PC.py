#coding:utf-8
# 导包
from selenium import webdriver
import time

# 1.打开浏览器
driver = webdriver.Chrome()
time.sleep(2)

# 2.获取网址(百度)
driver.get("http://www.baidu.com")

# 3.找到输入框，通过id进行元素定位
search = driver.find_element_by_id("kw")

# 4.输入想要搜素的关键词--元素操作
search.send_keys("?")
time.sleep(2)

# 找到提交按钮，元素定位
button = driver.find_element_by_id("su")
# 点击提交按钮
button.click()
time.sleep(2)

# 读取搜素结果的标题
title = driver.title
print(title)


# 断言，验证页面效果，如果不加就会直接关了
assert "符号" in title
# 关闭浏览器
driver.quit()
