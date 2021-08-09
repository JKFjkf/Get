import requests

url = 'http://www.baidu.com'
data = requests.get(url)
print(data.text)

#url = input('输入你的网址：')
#data = requests.get(url)
#print(data.status_code)
#print(data.text)