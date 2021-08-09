import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.baidu.com/")
r.encoding = r.apparent_encoding
demo = r.text
soup = BeautifulSoup(demo, "html.parser")
print(soup.a.prettify())