# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import AuthorItem


class AuthorSpider(scrapy.Spider):
    name = 'author'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        # follow links to author pages
        for href in response.css('.author + a::attr(href)'):
            yield response.follow(href, self.parse_author)

        # follow pagination links
        href = response.css('li.next a::attr(href)').get()
        if href is not None:
            yield response.follow(href, self.parse)

    def parse_author(self, response):
        item = AuthorItem()
        item['name'] = response.css('h3.author-title::text').get()
        item['birthdate'] = response.css('.author-born-date::text').get()
        item['bio'] = response.css('.author-description::text').get()
        yield item
