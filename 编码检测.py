import chardet
import requests
data = requests.get('http://www.baidu.com')

chardet = chardet.detect(data.content)#检测编码
print(chardet)
data.encoding=chardet['encoding']#指定编码
print(data.text)