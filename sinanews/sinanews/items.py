# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SinanewsItem(scrapy.Item):
    """
    定义item
    item的构成有:
            导航页的title, url
                分类页面下的title, url
                    分类下的文章链接
                    分类下的文章 head,content
    """
    # define the fields for your item here like:
    # name = scrapy.Field()
    parent_title = scrapy.Field()
    parent_url = scrapy.Field()

    sub_title = scrapy.Field()
    sub_url = scrapy.Field()

    sub_file_name = scrapy.Field()

    sub_sub_url = scrapy.Field()

    head = scrapy.Field()
    content = scrapy.Field()
