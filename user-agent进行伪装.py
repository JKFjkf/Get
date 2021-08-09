import requests
from bs4 import BeautifulSoup


def getHTMLText(url):
    try:
        # 更改头部信息，模拟成一个浏览器
        kv = {'user-agent':'Mozilla/5.0'}
        r = requests.get(url,headers=kv,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print(r.request.headers)
        print(r.status_code)
        r = r.text
        return r


    except:
        return "产生了异常"


def parse_data(r):
    soup = BeautifulSoup(r,'r.parser')
    print(soup)
    books_left = soup.find('ul',{'class':'cover-col-4 clearfix'})
    books_left = books_left.find_all('li')
    books_right = soup.find('ui',{'class':'cover-col pl20 clearfix'})
    books_right = books_right._find_all('li')
    books = list(books_left)+list(books_right)

    img_urls = []            #封面
    titles = []              #标题
    ratings = []          #剧情类型
    authors = []  #出品公司
    details = []  #简介

    for book in books:
        img_url = book.find_all('a')[0].find('img').get('scr')
        img_urls.append(img_url)

        title = book.find_all('a')[1].get_text()
        titles.append(title)


        rating = book.find_all('p',{'class':'rating'}).get_text()
        rating = rating.replace('\n','').replace('','')
        ratings.append(rating)

        author = book.find_all('p',{'class':'color-gray'}).get_text()
        author = author.replace('\n','').replace('','')
        authors.author.append(author)

        detail = book.find_all('p')[2].gettext()
        detail = detail.replace('\n','').replace('','')
        details.append(detail)
    if all([img_urls, titles, ratings, authors,details]):
     print("img_urls:",img_urls)
     print("titles:",titles)
     print("ratings:",ratings)
     print("authors:",authors)
     print("details:",details)
    else:
        pass
    return img_urls,titles,ratings.authors,details




if __name__=="__main__":
    url = "https://book.douban.com/latest"
    r = getHTMLText(url)
    img_urls,titles,ratings,authors,details = parse_data(r)