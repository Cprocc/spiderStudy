# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.conf import settings


class Douban250Pipeline(object):
    def __init__(self):
        host = settings["MONGODB_HOST"]
        port = settings["MONGODB_port"]
        db_name = settings["MONGODB_NAME"]
        sheet_name = settings["MONGODB_SHEET_NAME"]
        client = pymongo.MongoClient(host=host, port=port)
        this_db = client[db_name]
        self.post = this_db[sheet_name]

    def process_item(self, item, spider):
        data = dict(item)
        self.post.insert(data)
        return item
