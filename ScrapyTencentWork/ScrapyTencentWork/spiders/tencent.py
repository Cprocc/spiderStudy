# -*- coding: utf-8 -*-
import scrapy
from ..items import ScrapytencentworkItem


# spider name can't the same with project name
class TencentSpider(scrapy.Spider):

    # 执行命令: spider crawl tencent
    name = 'tencent'
    allowed_domains = ['tencent.com']
    url = "https://hr.tencent.com/position.php?&start="
    page_number = 0

    start_urls = [url + str(page_number)]

    def parse(self, response):
        """
        负责解析返回的网页数据response，提取结构化数据生成item
        生成下一个需要的url
        :param response:
        :return:
        """
        for each in response.xpath("//tr[@class='even'] | //tr[@class='odd']"):

            # 初始化一个ScrapytencentWorkItem对象
            item = ScrapytencentworkItem()

            # 选择器对象，extract() 去除unicode 对象，字符串列表
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
