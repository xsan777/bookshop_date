# -*- coding: utf-8 -*-
import scrapy


class DataSpider(scrapy.Spider):
    name = 'data'
    allowed_domains = ['quanshuwang.com']
    start_urls = ['http://quanshuwang.com/']

    def parse(self, response):
        pass
