# -*- coding: utf-8 -*-
import scrapy


class OnthesnowSpider(scrapy.Spider):
    name = "onthesnow"
    allowed_domains = ["onthesnow.com"]
    start_urls = (
        'http://www.onthesnow.com/ski-resort.html',
    )

    def parse(self, response):
        pass
