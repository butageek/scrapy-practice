# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FlixsterItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class MovieItem(scrapy.Item):
    title = scrapy.Field()
    director = scrapy.Field()
    duration = scrapy.Field()
    release_date = scrapy.Field()
    tomatometer = scrapy.Field()
    audience_score = scrapy.Field()
