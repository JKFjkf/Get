import requests
import urllib.parse
import time
import logging
from bs4 import BeautifulSoup


url = 'http://touch.dujia.qunar.com/depCities.qunar'
strhtml = requests.get(url)
dep_dict = strhtml.json()
for dep_item in dep_dict['data']:
    for dep in dep_dict['data'][dep_item]:
        a = []
        print(dep)
        url = 'http://m.dujia.qunar.com/golfz/sight/arriveRecommend?dep={}&exclude=&extensionImg=255,175'.format(urllib.parse.quote(dep))
        time.sleep(1)
        strhtml = requests.get(url)
        arrive_dict = strhtml.json()
        #print(arrive_dict)
        for arrive_item in arrive_dict['data']:
            for arrive_item_1 in arrive_item['subModules']:
                for query in arrive_item_1['items']:
                    if query['query'] not in a:
                        a.append(query['query'])
                        #print(query['query'])
        for item in a:
            url = 'https://touch.dujia.qunar.com/list?modules=list,bookingInfo&dep={}&query={}&mtype=all&ddt=false&mobFunction=%E6%89%A9%E5%B1%95%E8%87%AA%E7%94%B1%E8%A1%8C&cfrom=zyx&it=FreetripTouchin&et=FreetripTouchch&date=&configDepNew=&needNoResult=true&originalquery={}&limit=0,20&includeAD=true&qsact=search'.format(urllib.parse.quote(dep),
                                                                                                                                                                                                                                                                                                                                   urllib.parse.quote(item),
                                                                                                                                                                                                                                                                                                                                   urllib.parse.quote(item))
            time.sleep(1)
            strhtml= requests.get(url)
            routeCount = int(strhtml.json()['data']['limit']['routeCount'])
            print(routeCount)
            for limit in range(0,routeCount,20):
                url = 'https://touch.dujia.qunar.com/list?modules=list,bookingInfo&dep={}&query={}&mtype=all&ddt=false&mobFunction=%E6%89%A9%E5%B1%95%E8%87%AA%E7%94%B1%E8%A1%8C&cfrom=zyx&it=FreetripTouchin&et=FreetripTouchch&date=&configDepNew=&needNoResult=true&originalquery={}&limit={},20&includeAD=true&qsact=search'.format(urllib.parse.quote(dep),
                                                                                                                                                                                                                                                                                                                                        urllib.parse.quote(item),
                                                                                                                                                                                                                                                                                                                                        urllib.parse.quote(item),limit)
                time.sleep(1)
                strhtml = requests.get(url)
                #res = strhtml.text
                #soup = BeautifulSoup(res,'lxml')
                #print(time.strftime('%y-%m-%d', time.localtime(time.time())))
                #print(dep)
                #print(item)
                #print(limit)
                #print(strhtml.json())
                try:
                    data = time.strftime('%y-%m-%d', time.localtime(time.time()))
                    dep = dep
                    arrive = item
                    limit = limit
                    result = str(strhtml.json)
                except Exception as e:
                    logging.error(e)
                    print('错误点：', e)