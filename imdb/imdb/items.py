# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ImdbItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # url = scrapy.Field()    #url
    # title = scrapy.Field()  #影片名

    video_title = scrapy.Field()
    video_rating = scrapy.Field()
    video_name = scrapy.Field()
    video_alias = scrapy.Field()
    video_director = scrapy.Field()
    video_actor = scrapy.Field()
    video_length = scrapy.Field()
    video_language = scrapy.Field()
    video_year = scrapy.Field()
    video_type = scrapy.Field()
    video_color = scrapy.Field()
    video_area = scrapy.Field()
    video_voice = scrapy.Field()
    video_summary = scrapy.Field()
    video_url = scrapy.Field()
