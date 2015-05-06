# -*- coding: utf-8 -*-
import scrapy

class SwimingPoolItem(scrapy.Item):
    name = scrapy.Field()
    address = scrapy.Field()
    tel = scrapy.Field()
    website = scrapy.Field()
    admission = scrapy.Field()
    county = scrapy.Field()
    latlong = scrapy.Field()
    pools = scrapy.Field()
    notes = scrapy.Field()
    teams = scrapy.Field()
    reviews = scrapy.Field()

class SwimmersguideSpider(scrapy.Spider):
    name = "swimmersguide"
    allowed_domains = ["swimersguide.com"]

    def start_requests(self):
        for i in range(25525):
            url = "http://www.swimmersguide.com/ViewFacility.aspx?fid={}".format(i)
            yield scrapy.Request(url,callback=self.parse)

    def parse(self, response):
        item=SwimingPoolItem()
        name=response.xpath(r'//*[@id="ctl00_MainContent_FacilityNameLabel"]/text()').extract()
        if len(name):
            item['name']=name[0]
            item['website']=response.xpath(r'//*[@id="ctl00_MainContent_WebaddressLabel"]//a/@href').extract()
            item['address']=response.xpath(r'//*[@id="ctl00_MainContent_StreetAddressLabel"]/text()').extract()[0]
            item['tel']=response.xpath(r'//*[@id="ctl00_MainContent_TelephoneLabel"]/text()').extract()[0]
            item['admission']=response.xpath(r'//*[@id="ctl00_MainContent_GeneralAdmissionsLabel"]/text()').extract()[0]
            item['county']=response.xpath(r'//*[@id="ctl00_MainContent_CountyLabel"]/text()').extract()
            item['latlong']=response.xpath(r'//*[@id="ctl00_MainContent_LatLongLabel"]/text()').extract()[0]
            item['notes']=response.xpath(r'//*[@id="ctl00_MainContent_NotesGV_ctl02_CommentLabel"]//text()').extract()
            item['reviews']=response.xpath(r'//*[@id="ctl00_MainContent_ReviewsGV"]//tr/td/text()').extract()
            item['pools']=response.xpath(r'//*[@id="ctl00_MainContent_PoolGV"]//tr/td/text()').extract()
            team=response.xpath(r'//*[@id="ctl00_MainContent_ClubGV"]//tr/td[2]/a')
            if team:
                item['teams']=zip(response.xpath(r'//*[@id="ctl00_MainContent_ClubGV"]//tr/td[1]/text()').extract(),
                                  response.xpath(r'//*[@id="ctl00_MainContent_ClubGV"]//tr/td[2]/a/text()').extract(),
                                  response.xpath(r'//*[@id="ctl00_MainContent_ClubGV"]//tr/td[2]/a/@href').extract())
            #item['teams']=response.xpath(r'//*[@id="ctl00_MainContent_PoolGV"]//tr/td/text()').extract()
            #for pool in response.xpath(r'//*[@id="ctl00_MainContent_PoolGV"]//tr/td[2]/text()').extract():
             #   item['pools'].append(pool.extract())
             #   ctl00_MainContent_NotesGV
            yield item