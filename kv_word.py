import requests


def getHTMLText(url):
    try:
        # 更改头部信息，模拟成一个浏览器
        kv_head = {'user-agent': 'Mozilla/5.0'}
        kv_word = {'wd': 'Python'}
        r = requests.get(url, params=kv_word, headers=kv_head, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print(r.request.url)

        return len(r.text)
    except:
        return "产生异常"


if __name__ == "__main__":
    url = 'https://www.baidu.com/s'
    print(getHTMLText(url))