from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

with webdriver.Chrome() as driver:
    wait = WebDriverWait(driver,10)
    driver.get('https://www.phei.com.cn/module/goods/wssd_index.jsp')
    libs = driver.find_elements_by_css_selector('#book_sort_area > ul:nth-child(1) > li')
    for i in libs:
        image = i.find_element_by_css_selector('p > a > img').get_attribute("src")
        book = i.find_element_by_css_selector('p.li_title > a').text
        author = i.find_element_by_css_selector('p.li_author.ng-binding').text.split("\n")[0]
        price = i.find_element_by_css_selector('p.li_author.ng-binding > i').text
        print([book,price,author,image])