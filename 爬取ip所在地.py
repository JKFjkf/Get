import requests

url = 'http://www.ip138.com/ips138.asp?ip='
try:
    kv = {'user-agent': 'Mozilla/5.0'}
    r = requests.get(url+'10.3.8.211',headers=kv,timeout=30)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[-500:])
except:
    print("爬取失败")