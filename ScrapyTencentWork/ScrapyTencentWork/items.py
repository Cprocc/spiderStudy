# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

# create models
class ScrapytencentworkItem(scrapy.Item):
    # define the fields for your item here like:
    position_name = scrapy.Field()
    position_link = scrapy.Field()
    position_type = scrapy.Field()
    position_number = scrapy.Field()
    position_location = scrapy.Field()
    publish_time = scrapy.Field()

