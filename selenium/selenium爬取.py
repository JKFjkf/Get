import requests
import urllib.parse
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
# WebDriverWait 库，负责循环等待
from selenium.webdriver.support.ui import WebDriverWait
# expected_conditions 类，负责条件出发
from selenium.webdriver.support import expected_conditions as EC
#制定网页结束加载条件

def get_url(url):
    time.sleep(5)
    return (requests.get(url))
if __name__ == '__main__':
    driver = webdriver.Chrome()
    dep_cities = ['北京','兰州','广东','上海','福建']
    for dep in dep_cities:
        res = get_url('http://m.dujia.qunar.com/golfz/sight/arriveRecommend?dep='+urllib.parse.quote(dep)+'&exclude=&extensionImg=255,175')
        arrive_dict = res.json()
        for arr_item in arrive_dict['data']:
            for arr_item_1 in arr_item['subModules']:
                for query in arr_item_1['items']:
                    driver.get('https://fh.dujia.qunar.com/?tf=package')

                    WebDriverWait(driver,timeout=10).until(EC.presence_of_all_elements_located((By.ID,"depCity")))
                    driver.find_element_by_xpath('//*[@id="depCity"]').clear()
                    driver.find_element_by_xpath('//*[@id="depCity"]').send_keys(dep)
                    driver.find_element_by_xpath('//*[@id="arrCity"]').send_keys(query['query'])
                    driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[3]/div/div[2]/div/a').click()
                    print('dep:%s arr:%s' %(dep,query['query']))
                    for i in range(20):
                        time.sleep(random.uniform(5,6))
                        pageBtns = driver.find_elements_by_xpath('//*[@id="app"]/div/main')
                        if pageBtns ==[]:
                            break

                        routes = driver.find_elements_by_xpath('//*[@id="app"]/div/main/div[1]/div')
                        for route in routes:
                            result = {
                                'data' : time.strftime('%Y-%m-%d',time.localtime(time.time())),
                                'dep' : dep,
                                'arrive' : query['query'],
                                'result' : route.text
                            }
                            print(result)

driver.close()