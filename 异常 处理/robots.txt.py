import urllib.robotparser

rp = urllib.robotparser.RobotFileParser()
rp.set_url('https://baidu.com/robots.txt')
print('\n',rp.read())


rp.can_fetch('Googlelebot','https://www.baidu.com/baidu')
print(rp)

rp.can_fetch('baiduspider','https://baidu.com/cpro')
print(rp)


def robot_check(robotstxt_url, headers, url):
    rp = urllib.robotparser()
    rp.set_url(robotstxt_url)
    rp.read()
    result = rp.can_fetch(headers['User-Agent'], url)

    return result


if __name__ == '__main__':
    for url in urls:
        if robot_check(robotstxt_url, url):
            data = get_data(url)