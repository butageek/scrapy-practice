# -*- coding: utf-8 -*-
import scrapy
from flixster.items import MovieItem


class TopSpider(scrapy.Spider):
    name = 'top'
    allowed_domains = ['flixster.com']
    start_urls = ['https://www.flixster.com/top-box-office']

    def parse(self, response):
        # follow links to movie pages
        for href in response.css('ul li a.focus-item__movie-tile::attr(href)'):
            yield response.follow(href, self.parse_movie)

    def parse_movie(self, response):
        movie = MovieItem()
        movie['title'] = response.css('h1::text').get()
        movie['director'] = response.css(
            'div[data-qa="info-brief"] dd[data-qa="director"]::text').get()
        movie['duration'] = response.css(
            'div[data-qa="info-brief"] dd[data-qa="runtime"]::text').get()
        movie['release_date'] = response.css(
            'div[data-qa="info-brief"] dd[data-qa="release-date"]::text').get()
        movie['tomatometer'] = response.css(
            'a[data-qa="critic"] span[data-qa]::text').get()
        movie['audience_score'] = response.css(
            'a[data-qa="audience"] span[data-qa]::text').get()
        yield movie
