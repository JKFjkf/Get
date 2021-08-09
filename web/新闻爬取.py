import requests
import parsel
from urllib.parse import urljoin

urls = ['https://www.phei.com.cn/xwxx/index_{}.shtml'.format(i) for i in range(53)]
for url in urls:
    res = requests.get(url)
    sel = parsel.Selector(res.content.decode("utf-8"))
    li = sel.css('.web_news_list  ul  li.li_b60')
    for news in li:
        title = news.css('p.li_news_title::text').extract_first()
        pub_time = news.css('span::text').extract_first()
        desc = news.css('p.li_news_summary::text').extract_first()
        image = news.css("div.li_news_line img::attr('src')").extract_first()
        full_image = urljoin(url,image)
        print(title,pub_time,desc,full_image)