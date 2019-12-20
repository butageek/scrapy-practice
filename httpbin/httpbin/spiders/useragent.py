# -*- coding: utf-8 -*-
import scrapy
import json


class UseragentSpider(scrapy.Spider):
    name = 'useragent'
    allowed_domains = ['httpbin.org']
    start_urls = ['https://httpbin.org/user-agent']

    def parse(self, response):
        print(json.loads(response.body))
