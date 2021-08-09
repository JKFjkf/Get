from selenium import webdriver
import time

zhengyi = webdriver.Chrome()
zhengyi.get('https://mail.qq.com/')

# 定位login_frame
zhengyi.switch_to.frame("login_frame")
zhengyi.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
# 定位账号、密码，并输入
zhengyi.find_element_by_xpath('//*[@id="u"]').send_keys("1920578919")
zhengyi.find_element_by_xpath('//*[@id="p"]').send_keys("yujie12138")
# 定位登录按钮
zhengyi.find_element_by_xpath('//*[@id="login_button"]').click()



