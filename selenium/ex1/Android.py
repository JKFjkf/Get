"""
学习目标：
    禁用浏览器的信息提示
    模拟移动端
    操作步骤
"""

# 导包
from selenium import webdriver

# 移动端的模拟
mobileEmulation={"deviceName":"iPhone X"}
chrome_options = webdriver.ChromeOptions()

# 添加实验选项  (排除交换器，开启自动化)
chrome_options.add_experimental_option("excludeSwitches",["enable-automation"])

# 添加实验选项   是否使用自动拓展功能 否
chrome_options.add_experimental_option("useAutomationExtension",False)

# 添加实验选项    移动端的模拟
chrome_options.add_experimental_option("mobileEmulation",mobileEmulation)

# 打开chrome浏览器
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.baidu.com")

