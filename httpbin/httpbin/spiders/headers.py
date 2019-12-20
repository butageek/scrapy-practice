# -*- coding: utf-8 -*-
import scrapy
import json


class HeadersSpider(scrapy.Spider):
    name = 'headers'
    allowed_domains = ['httpbin.org']
    start_urls = ['https://httpbin.org/headers']

    def parse(self, response):
        print(json.loads(response.body))
