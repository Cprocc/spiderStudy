# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class SinanewsPipeline(object):
    def process_item(self, item, spider):
        sub_sub_urls = item['sub_sub_url']

        file_name = sub_sub_urls[7:-6].replace('/', '_')
        file_name += ".txt"

        fp = open(item['sub_file_name'] + '/' + file_name, 'w', encoding="utf-8")
        fp.write(item['content'])
        fp.close()

        return item
