# --*-- coding: utf-8 --*--
from scrapy import cmdline
cmdline.execute("scrapy crawl music -o music.csv".split())
cmdline.execute("scrapy crawl video -o video.csv".split())