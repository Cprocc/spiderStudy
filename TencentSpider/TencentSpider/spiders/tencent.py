# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import TencentspiderItem


class TencentSpider(CrawlSpider):
    name = 'tencent'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['http://hr.tencent.com/position.php?&start=0#a']

    # Response里的链接提取规则，返回符合匹配规则的链接匹配对象
    page_link = LinkExtractor(allow="start=\d+")

    rules = [
        Rule(page_link, callback='parse_item', follow=True),
    ]

    @staticmethod
    def parse_item(response):
        for each in response.xpath("//tr[@class='even'] | //tr[@class='odd']"):
            # 初始化模型对象
            item = TencentspiderItem()

            item["position_name"] = each.xpath("./td[1]/a/text()").extract()[0]
            item['position_link'] = each.xpath("./td[1]/a/@href").extract()[0]
            item['position_type'] = each.xpath("./td[2]/text()").extract()
            item['position_number'] = each.xpath("./td[3]/text()").extract()[0]
            item['position_location'] = each.xpath("./td[4]/text()").extract()[0]
            item['publish_time'] = each.xpath("./td[5]/text()").extract()[0]

            yield item
