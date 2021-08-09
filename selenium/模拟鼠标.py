import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium .webdriver.chrome.options import Options

#chorme_options = Options()
#chorme_options.add_argument('--headless')
#with webdriver.Chrome(options = chorme_options) as driver:
with webdriver.Chrome() as driver:
    driver.get('https://www.phei.com.cn/module/goods/wssd_index.jsp')
    footer = driver.find_element_by_class_name("web_book_footer")
    ActionChains(driver).move_to_element(footer).perform()
    time.sleep(10)