# -*- coding: utf-8 -*-
import scrapy
from ..items import ScrapytencentworkItem


class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['tencent.com']
    url = "https://hr.tencent.com/position.php?&start="
    page_number = 0

    start_urls = [url + str(page_number)]

    def parse(self, response):
        for each in response.xpath("//tr[@class='even'] | //tr[@class='odd']"):
            item = ScrapytencentworkItem()
            item["position_name"] = each.xpath("./td[1]/a/text()").extract()[0]
            item['position_link'] = each.xpath("./td[1]/a/@href").extract()[0]
            item['position_type'] = each.xpath("./td[2]/text()").extract()
            item['position_number'] = each.xpath("./td[3]/text()").extract()[0]
            item['position_location'] = each.xpath("./td[4]/text()").extract()[0]
            item['publish_time'] = each.xpath("./td[5]/text()").extract()[0]

            yield item

        if self.page_number <= 2860:
            self.page_number += 10

        yield scrapy.Request(self.url + str(self.page_number), callback=self.parse)
