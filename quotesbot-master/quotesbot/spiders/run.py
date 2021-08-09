from scrapy import cmdline
cmdline.execute("scrapy crawl toscrape-xpath -o quotes.json".split())