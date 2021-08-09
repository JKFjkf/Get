import requests


def getHTMLText(url):
    try:
        path = 'E:/常用/图/图集/abc.jpeg'
        # 更改头部信息，模拟成一个浏览器
        kv_head = {'user-agent': 'Mozilla/5.0'}
        r = requests.get(url, headers=kv_head, timeout=30)
        print(r.status_code)
        # 将获得的存入路径中,r.content是二进制文件
        with open(path, 'wb') as f:
            f.write(r.content)
        f.close()
        return len(r.text)
    except:
        return "产生异常"

if __name__ == "__main__":
        url = 'https://b-ssl.duitang.com/uploads/item/201601/25/20160125170559_SPKF2.jpeg'
        print(getHTMLText(url))