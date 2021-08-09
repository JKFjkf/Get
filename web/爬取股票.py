import requests
from bs4 import BeautifulSoup
import re
import time

#url = 'http://quote.stockstar.com/stock/ranklist_a_3_1_1.html'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OSX10_14_2) AppleWebKit/537.36(KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
for i in range(1,11):
    time.sleep(1)
    url = 'http://quote.stockstar.com/stock/ranklist_a_3_1_'+str(i)+'.html'
    res = requests.get(url,headers=headers,timeout=30)
    soup = BeautifulSoup(res.text,'lxml')
    datas = soup.find_all('tr')
    print(datas)
    for data in datas:
        code = data.find('td',class_='align_center ').find('a')
        print(code)
        abbr = data.find('td',class_='align_center').find('a')
        print(abbr)
        Circulation_market_value = data.find('td',class_='align_right ')
        print(Circulation_market_value)
        Total_market_value = data.find('td',class_='align_right select')
        print(Total_market_value)
        Crculating_share_capital = data.find('td',class_='align_right ')
        print(Crculating_share_capital)
        Total_equity = data.find('td',class_='align_right ')
        print(Total_equity)


        #if all([code,abbr,Circulation_market_value,Total_market_value,Crculating_share_capital,Total_equity]):
        #print('代码：'+code)
        #print('链接：'+code['herf'])
        #print('简称:'+abbr.text)
        #print('流通市值：'+Circulation_market_value.text)
        #print('总市值：'+Total_market_value.text)
        #print('流通股本：'+Crculating_share_capital.text)
        #print('总股本:'+Total_equity.text)

        #else:
        #   pass
