import requests
import  builtwith
from fake_useragent import UserAgent
from bs4 import BeautifulSoup



ua = UserAgent()
print(ua.chorm)
try:
    kv_head = headers = {'User-Agent': ua.chrome}
    #print(builtwith.parse(url))

    url = 'https://book.douban.com/latest'
    data = requests.get(url,headers=kv_head,timeout=100)
#data.raise_for_status()
    print(data.status_code)
except Exception as e:
    print(e)
#soup = BeautifulSoup(data.text,'lxml')
#print(soup)
html=data.text


soup = BeautifulSoup(html,'lxml')
print(soup)
books = soup.select('#content > div > div.article > ul > li:nth-child(1) > div > h2 > a')

#for item in books:
#    result = {
#        'title': item.get_text,
#        'link': item.get('href'),

#    }
#    print(result)

#books_right = soup.find('ui',{'class':'cover-col pl20 clearfix'}).find_all('li')
#books = list(books_left)+list(books_right)

img_urls = []          #封面
titles = []            #标题
ratings = []           #评分
authors = []           #作者
details = []           #简介

for book in books:
    img_url = book.find_all('a')[0].find('img').get('scr')
    img_urls.append(img_url)

    title = book.find_all('a')[1].get_text()
    titles.append(title)


    rating = book.find_all('p',class_='rating').find('span',clss_='font-small  color-lightgray').get_text()
    rating = rating.replace('\n','').replace('','')
    ratings.append(rating)

    author = book.find_all('p',{'class':'color-gray'}).get_text()
    author = author.replace('\n','').replace('','')
    authors.author.append(author)

    detail = book.find_all('p')[2].gettext()

    detail = detail.replace('\n','').replace('','')
    details.append(detail)

    if all([img_urls, titles, ratings, authors, details]):#表示都不为空
        print("封面:",img_urls)
        print("标题:",titles)
        print("评分:",ratings)
        print("作者:",authors)
        print("简介:",details)
        print('\n' + '******************************' + '\n')
    else:
        pass

