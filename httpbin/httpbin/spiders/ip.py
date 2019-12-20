# -*- coding: utf-8 -*-
import scrapy
import json


class IpSpider(scrapy.Spider):
    name = 'ip'
    allowed_domains = ['httpbin.org']
    start_urls = ['https://httpbin.org/ip']

    def parse(self, response):
        print(json.loads(response.body))
