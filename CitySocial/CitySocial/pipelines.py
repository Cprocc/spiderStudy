# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


class CitysocialPipeline(object):
    def __init__(self):
        self.filename = open("citySocialQA.json", "w", encoding="utf-8")

    def open_spider(self, spider):
        pass

    # 继承object类，必写的方法
    def process_item(self, item, spider):
        text = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.filename.write(text.encode("utf-8", errors="ignore").decode("utf-8", errors="ignore"))
        return item

    def close_spider(self, spider):
        self.filename.close()
