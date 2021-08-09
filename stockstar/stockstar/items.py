# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst


class StockstarItemLoader(ItemLoader):
    default_output_processor = TakeFirst

class StockstarItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    code = scrapy.Field()#股票代码
    abbr = scrapy.Field()#股票简称
    Circulation_market_value = scrapy.Field()#流通市值
    Total_market_value = scrapy.Field()#总市值
    Circulating_share_capital = scrapy.Field()#流通股本
    Total_equity= scrapy.Field()#总股本

