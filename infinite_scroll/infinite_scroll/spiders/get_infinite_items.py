# -*- coding: utf-8 -*-
import scrapy


class GetInfiniteItemsSpider(scrapy.Spider):
    name = 'get_infinite_items'
    allowed_domains = ['scrapingclub.com']
    start_urls = ['https://scrapingclub.com/exercise/list_infinite_scroll/']

    def parse(self, response):
        for product in response.css('div.row.my-4 > div'):
            name = product.css('a::text').get()
            price = product.css('h5::text').get()

            yield {
                'name': name,
                'price': price
            }

        next_page = response.css('a.page-link.next-page::attr(href)').get()

        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
