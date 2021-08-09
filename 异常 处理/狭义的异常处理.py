import requests
import urllib.robotparser

urls = ["http://news.baidu.com","http://www.baidesss.com","http://news.baidu.com","http://datahonor.com/404","http://httpstat.us/500"]

def get_data(url):
    try:

        data = requests.get(url)
    except requests.exceptions.ConnectionError as e:
        print("请求错误。url：\n",url)
        print("错误详情：\n",e)
        data = None
        #exit(1)
    return data

def robot_check(robotstxt_url,headers,url):
    rp = urllib.robotparser()
    rp.set_url(robotstxt_url)
    rp.read()
    result = rp.can_fetch(headers['User-Agent'],url)

    return result


if __name__ == '__main__':
    for url in urls:
        get_data(url)
