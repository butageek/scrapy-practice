# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
import redis
from scrapy.exceptions import DropItem


class FlixsterPipeline(object):
    def process_item(self, item, spider):
        return item


class DatabasePipeline(object):
    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings)

    def __init__(self, settings):
        self.mongo_uri = settings.get('MONGO_URI')
        self.mongo_db = settings.get('MONGO_DB')

    def open_spider(self, spider):
        self.mongo_client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.mongo_client[self.mongo_db]
        self.redis_client = redis.Redis()

    def close_spider(self, spider):
        self.mongo_client.close()

    def process_item(self, item, spider):
        if self.redis_client.sadd('movie_title', item['title']) == 1:
            self.db['top_movie'].insert_one(dict(item))
            return item
        else:
            raise DropItem(f"Duplicate item found: {item['title']}")
