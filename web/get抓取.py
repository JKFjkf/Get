import requests

url = 'http://www.cntour.cn'
re = requests.get(url)
print(re.text)