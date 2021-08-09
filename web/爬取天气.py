import requests
from bs4 import BeautifulSoup

url = 'https://devapi.qweather.com/v7/weather/now?location=101010100&key=1b43ddd0d74240d1ad61e29e34ad1aeb&range=cn'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OSX10_14_2) AppleWebKit/537.36(KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
res = requests.get(url,headers=headers,timeout=10)
res.encoding = 'utf-8'
data = res.text
#data1 = data.split('\r')
#print(data1)
#print(data)
soup = BeautifulSoup(data,'lxml')
print(soup)