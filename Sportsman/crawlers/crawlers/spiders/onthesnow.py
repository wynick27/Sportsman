# -*- coding: utf-8 -*-
import scrapy
from scrapy import log

class OnthesnowItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    trails =scrapy.Field()
    name = scrapy.Field()
    terrain_parks=scrapy.Field()
    lifts=scrapy.Field()
    summit=scrapy.Field()
    base=scrapy.Field()
    drop=scrapy.Field()
    website=scrapy.Field()
    snow_making=scrapy.Field()
    skiable_area=scrapy.Field()
    longest_run=scrapy.Field()
    fast_eight=scrapy.Field()
    fast_sixes=scrapy.Field()
    fast_quads=scrapy.Field()
    quad=scrapy.Field()
    trams=scrapy.Field()
    triple=scrapy.Field()
    double=scrapy.Field()
    surface=scrapy.Field()
    beginner=scrapy.Field()
    intermediate=scrapy.Field()
    advanced=scrapy.Field()
    expert=scrapy.Field()

class OnthesnowSpider(scrapy.Spider):
    name = "onthesnow"
    allowed_domains = ["onthesnow.com"]
    start_urls = (
        'http://www.onthesnow.com/ski-resort.html',
    )

    def parse(self, response):
        for skiarea in response.css('#left_rail tr>td .name'):
            url=skiarea.xpath('a/@href').extract()
            log.msg(url[0])
            dict={'name': skiarea.xpath('a/text()').extract()[0]}
            yield scrapy.Request('http://www.onthesnow.com' + url[0], callback=self.analyze,meta=dict)

    def analyze(self,response):
        item = OnthesnowItem()
        item['name']=response.meta['name']
        dict={'trails': r'//*[@id="resort_terrain"]/ul[2]/li[1]/p[2]/text()', 
        'terrain_parks': r'//*[@id="resort_terrain"]/ul[2]/li[2]/p[2]/text()',
        'lifts':r'//*[@id="resort_lifts"]/ul[2]/li[4]/text()',
        'summit':'//*[@id="resort_elevation"]/ul/li[1]/div[1]/text()',
        'base':r'//*[@id="resort_elevation"]/ul/li[2]/div[1]/text()',
        'drop':r'//*[@id="resort_elevation"]/ul/li[3]/div[1]/text()',
        'snow_making':r'//*[@id="resort_terrain"]/ul[3]/li/p[2]/text()',
        'skiable_area':r'//*[@id="resort_terrain"]/ul[2]/li[4]/p[2]/text()',
        'longest_run':r'//*[@id="resort_terrain"]/ul[2]/li[3]/p[2]/text()',
        'trams' : r'//*[@id="resort_lifts"]/ul[1]/li[1]/text()',

        'fast_eight' : r'//*[@id="resort_lifts"]/ul[1]/li[2]/text()',
        'fast_sixes' : r'//*[@id="resort_lifts"]/ul[1]/li[3]/text()',
        'fast_quads' : r'//*[@id="resort_lifts"]/ul[1]/li[4]/text()',
        'quad' : r'//*[@id="resort_lifts"]/ul[1]/li[5]/text()',

        'triple' : r'//*[@id="resort_lifts"]/ul[2]/li[1]/text()',
        'double' : r'//*[@id="resort_lifts"]/ul[2]/li[2]/text()',
        'surface' : r'//*[@id="resort_lifts"]/ul[2]/li[3]/text()',
        'beginner':r'//*[@id="resort_terrain"]/ul[1]/li[1]/p[2]/text()',
        'intermediate':r'//*[@id="resort_terrain"]/ul[1]/li[2]/p[2]/text()',
        'advanced':r'//*[@id="resort_terrain"]/ul[1]/li[3]/p[2]/text()',
        'expert':r'//*[@id="resort_terrain"]/ul[1]/li[4]/p[2]/text()',
        'website':r'//*[@id="content_pos"]/div[2]/div[1]/ul/li[2]/p/a'}
        for key,value in dict.iteritems():
            result=response.xpath(value).extract()
            if len(result) == 0 :
                result=""
            else:
                result=result[0].strip()
            item[key] =  result
        yield item


