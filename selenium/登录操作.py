import requests
import urllib.parse
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def get_url(url):
    time.sleep(5)
    return (requests.get(url))


if __name__ == '__main__':
    driver = webdriver.Chrome()
    #res = get_url('https://www.bilibili.com/')
    driver.get('https://www.bilibili.com/')
    WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.ID, "nav_searchform")))
    driver.find_element_by_xpath('//*[@id="internationalHeader"]/div[1]/div/div[3]/div[2]/div[1]').click()
    driver.find_element_by_xpath('//*[@id="login-username"]"]').send_keys('17393127047')
    driver.find_element_by_xpath('//*[@id="login-passwd"]').send_keys('szx001')
    driver.find_element_by_xpath('//*[@id="geetest-wrap"]/div/div[5]/a[1]').click()
    #driver.close()