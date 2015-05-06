# -*- coding: utf-8 -*-
import scrapy

class TrailItem(scrapy.Item):
    name = scrapy.Field()
    address = scrapy.Field()
    link = scrapy.Field()
    difficulty = scrapy.Field()
    length = scrapy.Field()
    types = scrapy.Field()


class SwimmersguideSpider(scrapy.Spider):
    name = "alltrails"
    allowed_domains = ["alltrails.com"]
    start_urls = (
        'http://alltrails.com/search?d=99999&l_min=&l_max=&dur_min=&dur_max=',
    )

    def parse(self, response):
        for trail in response.xpath(r'//*[@id="trail-results"]/li'):
            item=TrailItem()
            item['name']=trail.xpath(r'//h3/a/text()').extract()[0]
            item['link']=trail.xpath(r'//h3/a/@href').extract()[0]
            item['address']=trail.xpath(r'//h4/text()').extract()[0]
            item['lenght']=trail.xpath(r'//h5/text()').extract()[0]
            item['difficulty']=trail.xpath(r'//h5/span/@data-tip').extract()[0]
            item['activities']=trail.xpath(r'//dl/dd/a/text()').extract()
            yield item
        next=response.xpath(r'//*[@class="next"]//a/@href').extract()
        if len(next):
            url = "http://alltrails.com/" + next[0]
            yield scrapy.Request(url,callback=self.parse)