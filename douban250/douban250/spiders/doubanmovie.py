# -*- coding: utf-8 -*-
import scrapy
from ..items import Douban250Item


class DoubanmovieSpider(scrapy.Spider):
    name = 'doubanmovie'
    allowed_domains = ['movie.douban.com']
    offset = 0
    url = "http://movie.douban.com/top250?start=" + str(offset)
    start_urls = [url]

    def parse(self, response):
        item = Douban250Item()
        movies = response.xpath("//div[@class='info']")
        for each in movies:
            item["title"] = each.xpath(".//span[@class='title'][1]/text()").extract()[0]
            item["bd"] = each.xpath(".//div[@class='bd']/p/text()").extract()[0]
            item["star"] = each.xpath(".//span[@class='rating_num']/text()").extract()[0]
            item["quote"] = each.xpath(".//div[@class='bd']//p[@class='quote']/span/text()").extract()

            yield item

        if self.offset < 225:
            self.offset += 25
            yield scrapy.Request(self.url + str(self.offset), callback=self.parse)
