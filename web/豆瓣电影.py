import requests
from bs4 import BeautifulSoup
import pymysql
import logging



def writeDb(sql, db_data=()):
    """
    连接mysql数据库（写），并进行写的操作
    """
    try:
        conn = pymysql.connect(host='localhost',
                               port=3306,
                               user='root',
                               password='123456',
                               db='python',
                               charset='utf8')
        cursor = conn.cursor()
    except Exception as e:
        print(e)
        logging.error('数据库连接失败:%s' % e)
        return False

    try:
        cursor.execute(sql, db_data)
        conn.commit()
    except Exception as e:
        conn.rollback()
        logging.error('数据写入失败:%s' % e)
        return False
    finally:
        cursor.close()
        conn.close()
    return True


#def get_data():
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36'}

for i in range(1,11):#因为一页只有25个电影简介，所以需要10页
    href='https://movie.douban.com/top250?start='+str((i-1)*25)+'&filter='
    res=requests.get(href,headers=headers)
    #头等信息
    html=res.text
    #def parase_data():
    soup=BeautifulSoup(html,'html.parser') #解析网页代码
    #需要爬取 序号，电影名，评分，推荐语，链接
    movies=soup.find('ol',class_='grid_view').find_all('li')
    for movie in movies:
        movie_num=movie.find('div',class_='pic').find('em') #电影序号
        movie_name=movie.find('div',class_='info').find('span',class_='title') #电影名称
        movie_star=movie.find('div',class_='star').find('span',class_='rating_num') #电影评分
        movie_recommend=movie.find('p',class_='quote') #电影推荐语
        movie_href=movie.find('div',class_='pic').find('a')#电影链接 movie_href['href']



        if all([movie_name,movie_href,movie_num,movie_star,movie_recommend]):#表示都不为空
            print('排行第'+movie_num.text+'的电影:'+'\n')
            print('电影名：'+movie_name.text.strip()+'\t'+'评分：'+movie_star.text)
            print('推荐语：'+movie_recommend.text+'\n')
            print('链接：'+movie_href.get['href'])
            print('\n'+'******************************'+'\n')


        else:
            pass

        try:
            a = movie_num.text
            b = movie_name.text.strip()
            c = movie_star.text
            d = movie_recommend.text
            e = movie_href['href']

            sql = """ INSERT INTO movie(
                        movie_name,
                        movie_href,
                        movie_num,
                        movie_star,
                        movie_recommend)
                  VALUES(%s,%s,%s,%s,%s) """
            data = (b, e, a, c, d)

            writeDb(sql, data)
        except Exception as e:
            logging.error(e)
            print('错误点：',e)

#def save_data(movie_num,movie_name,movie_star, movie_recommend,movie_href):
    #result['电影名'] = movie_name.text.strip()
    #result['评分'] = movie_star.text
    #result['推荐语'] = movie_recommend.text
    #result['链接'] = movie_href['href']
    #result.to_csv('result.csv',index=None)