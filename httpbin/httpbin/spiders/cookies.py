# -*- coding: utf-8 -*-
import scrapy
import json


class CookiesSpider(scrapy.Spider):
    name = 'cookies'
    allowed_domains = ['httpbin.org']
    start_urls = ['https://httpbin.org/cookies']

    def parse(self, response):
        print(json.loads(response.body))
