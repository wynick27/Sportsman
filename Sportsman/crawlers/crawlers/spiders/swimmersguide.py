# -*- coding: utf-8 -*-
import scrapy


class SwimmersguideSpider(scrapy.Spider):
    name = "swimmersguide"
    allowed_domains = ["swimersguide.com"]
    start_urls = (
        'http://www.swimersguide.com/',
    )

    def parse(self, response):
        for country in response.xpath(r'//*[@id="ctl00_MainContent_NationLB"]/option'):
            pass