# --*-- coding: utf-8 --*--
from scrapy import cmdline
cmdline.execute("scrapy crawl stock -o items.json".split())