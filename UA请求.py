import requests

url = 'https://www.amazon.cn/'
data = requests.get(url)
print(data.text)