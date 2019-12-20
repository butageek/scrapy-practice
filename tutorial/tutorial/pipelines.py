# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
import redis
from scrapy.exceptions import DropItem


class TutorialPipeline(object):
    def process_item(self, item, spider):
        return item


class DatabasePipeline(object):
    collection = 'quotes'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        self.redis_client = redis.Redis()

    @classmethod
    def from_crawler(cls, crawler):
        settings = crawler.settings
        return cls(
            mongo_uri=settings.get('MONGO_URI'),
            mongo_db=settings.get('MONGO_DB', 'tutorial')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        if self.redis_client.sadd('tutorial:text', item['text']) == 1:
            self.db[spider.name].insert_one(dict(item))
            return item
        else:
            raise DropItem(f"Duplicate item found {item['text']}")
