# -*- coding: utf-8 -*-
import scrapy
from ..items import SinanewsItem
import os


class SinaSpider(scrapy.Spider):
    name = 'sina'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://news.sina.com.cn/guide/']

    def parse(self, response):
        """
        解析所有大类title,url; 小类title,url。获取小类中文章的url,交给content_parse处理
        :param response:
        :return:
        """

        items = []
        # 取出大类的链接和标题
        parent_urls = response.xpath('//div[@id="tab01"]/div/h3/a/@href').extract()
        parent_titles = response.xpath('//div[@id="tab01"]/div/h3/a/text()').extract()

        # 所有小类的链接和标题
        sub_urls = response.xpath('//div[@class="clearfix"]/ul/li/a/@href').extract()
        sub_titles = response.xpath('//div[@class="clearfix"]/ul/li/a/text()').extract()

        # 爬取所有大类
        for i in range(0, len(parent_titles)):
            parent_file_name = "./Data/" + parent_titles[i]

            if not os.path.exists(parent_file_name):
                os.makedirs(parent_file_name)
            # 爬取所有小类
            for j in range(0, len(sub_urls)):
                item = SinanewsItem()

                item['parent_title'] = parent_titles[i]
                item['parent_url'] = parent_urls[i]

                # 检查小类的格式是否和大类在同一个域下
                if_belong = sub_urls[j].startswith(item['parent_url'])

                if if_belong:
                    sub_file_name = parent_file_name + "/" + sub_titles[j]

                    if not os.path.exists(sub_file_name):
                        os.makedirs(sub_file_name)

                    item['sub_url'] = sub_urls[j]
                    item['sub_title'] = sub_titles[j]
                    item['sub_file_name'] = sub_file_name

                    items.append(item)

        for item in items:
            yield scrapy.Request(url=item['sub_url'], meta={'meta_1': item}, callback=self.sub_pares)

    def sub_pares(self, response):
        """
        对于返回的小类sub_url,进行递归请求
        :param response:
        :return:
        """
        meta_1 = response.meta['meta_1']

        # 取出小类里的所有子链接
        sub_sub_urls = response.xpath('//a/@href').extract()
        items = []

        for i in range(0, len(sub_sub_urls)):
            if_belong = sub_sub_urls[i].endswith('.shtml') and sub_sub_urls[i].startswith(meta_1['parent_url'])

            if if_belong:
                item = SinanewsItem()
                item['parent_title'] = meta_1['parent_title']
                item['parent_url'] = meta_1['parent_url']
                item['sub_url'] = meta_1['sub_url']
                item['sub_title'] = meta_1['sub_title']
                item['sub_file_name'] = meta_1['sub_file_name']
                item['sub_sub_url'] = sub_sub_urls[i]

                items.append(item)

        for item in items:
            yield scrapy.Request(url=item['sub_sub_url'], meta={'meta_2': item}, callback=self.content_parse)

    @staticmethod
    def content_parse(response):
        """
        根据url, 获取文章标题和内容
        :param response:
        :return:
        """

        item = response.meta['meta_2']
        content = ''
        head = response.xpath('//h1[@class="main-title"]/text()')
        content_list = response.xpath('//div[@class="article"]/p/text()').extract()

        for content_one in content_list:
            content += content_one

        item['head'] = head
        item['content'] = content

        yield item
