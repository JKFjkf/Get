import requests

url = 'https://www.baidu.com'
r = requests.get(url)
print(r.encoding)
r.encoding = r.apparent_encoding
print(r.encoding)
print(r.apparent_encoding)
