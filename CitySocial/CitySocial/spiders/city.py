# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import CitysocialItem


class CitySpider(CrawlSpider):
    name = 'city'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=0']

    # If callback is None follow defaults to True, otherwise it defaults to False.
    rules = (
        Rule(LinkExtractor(allow=r'type=4&page=\d+')),
        Rule(LinkExtractor(allow=r'/html/question/\d+/\d+.shtml'), callback='parse_item'),
    )

    @staticmethod
    def parse_item(response):
        item = CitysocialItem()

        item["name"] = response.xpath('//div[contains(@class, "pagecenter p3")]//strong/text()').extract()[0]
        item["question_number"] = item["name"].split(' ')[-1].split(":")[-1]
        content = response.xpath('//div[@class="contentext"]/text()').extract()

        if len(content) == 0:
            content = response.xpath("//div[@class='c1 text14_2']/text()").extract()
            item["content"] = "".join(content).strip()
        else:
            item["content"] = "".join(content).strip()
        item["url"] = response.url

        yield item
