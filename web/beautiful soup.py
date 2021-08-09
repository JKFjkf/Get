import requests
from bs4 import BeautifulSoup
import re

url = 'http://www.cntour.cn/'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OSX10_14_2) AppleWebKit/537.36(KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
#proxies = {
#    'http':'http://10.10.1.10:3128',
#   'http':'http://10.10.1.10:1028'
#}
res = requests.get(url,headers=headers,timeout=30)
soup = BeautifulSoup(res.text,'lxml')
data = soup.select('#main > div > div.mtop.firstMod.clearfix > div.centerBox > ul.newsList > li > a')
print(data)
for item in data:
    result = {
        'title': item.get_text,
        'link': item.get('href'),
        'ID':re.findall('\d+',item.get('href'))
    }
    print(result)