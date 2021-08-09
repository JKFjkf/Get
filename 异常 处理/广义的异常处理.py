import requests
import time

urls = ["http://httpstat.us/500"]

def get_data(url,number_retries=3):
    try:
        data = requests.get(url,timeout = 5)
        print(data.status_code)
    except requests.exceptions.ConnectionError as e:
        print("错误请求，url：\n",url)
        print("错误详情：\n",e)
        data = None

    if(data != None) and ( 500 <= data.status_code<600):
        if (number_retries > 0):
            print("服务器错误，正在重试...")
            time.sleep(1)
            number_retries -= 1
            get_data(url,number_retries)
    return data



if __name__ == '__main__':
    for url in urls:
        get_data(url)