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

for i in range(1, 100):
    url = 'https://maoyan.com/board/4?offset=' + str(i)

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OSX10_14_2) AppleWebKit/537.36(KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
    res = requests.get(url, headers=headers)
    html = res.text
    soup = BeautifulSoup(html, 'html.parser')
    tables = soup.find_all('dd')
    for tabel in tables:
        rank = tabel.find(name='i').get_text()
        name = tabel.find(name='p', class_='name').get_text()
        star = tabel.find(name='p', class_='star').get_text().strip()[3:]
        score = tabel.find(name='p', class_='score').get_text()
        time = tabel.find(name='p', class_='releasetime').get_text().strip()[5:]

        print('排名：',int(rank)-1)
        print('电影名：',name)
        print('明星：',star)
        print('分数：',score)
        print('上映时间：',time)
        print('\n' + '******************************' + '\n')

        try:

            sql = """ INSERT INTO move_1(
                        排名,
                        电影名,
                        参演,
                        分数,
                        上映时间)
                  VALUES(%s,%s,%s,%s,%s) """

            data = (int(rank)-1,name,star,score,time)
            writeDb(sql, data)
        except Exception as e:
            logging.error(e)
            print('错误点：',e)
