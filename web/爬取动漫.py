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

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OSX10_14_2) AppleWebKit/537.36(KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
for i in range(1,11):
    url = 'https://www.agefans.tv/rank?tag=catyear&value=&page='+str(i)
    res = requests.get(url,headers=headers,timeout=10)
    soup = BeautifulSoup(res.text,'lxml')
    datas = soup.find_all('li',class_='rank_text')
    print(datas)
    for data in datas:
        cartoon_number = data.find('span')
        cartoon_name = data.find('a').find('span')
        cartoon_href = data.find('a')
        cartoon_rank = data.find('span',class_='rank_value asciifont')

        print(cartoon_number.text)
        print(cartoon_name.text)
        print('https://www.agefans.tv'+cartoon_href.get('href'))
        print(cartoon_rank.text)
        print('\n' + '******************************' + '\n')
        cartoon_href = 'https://www.agefans.tv'+cartoon_href.get('href')
        try:

            sql = """ INSERT INTO cartoon(
                        cartoon_number,
                        cartoon_name,
                        cartoon_href,
                        cartoon_rank)
                  VALUES(%s,%s,%s,%s) """
            data = (cartoon_number.text, cartoon_name.text, cartoon_href, cartoon_rank.text)
            writeDb(sql, data)
        except Exception as e:
            logging.error(e)
            print('错误点：',e)




#container > div.div_right.baseblock > div > div.baseblock > div > ul:nth-child(1) > li:nth-child(1)
#container > div.div_right.baseblock > div > div.baseblock > div > ul:nth-child(1) > li:nth-child(2)