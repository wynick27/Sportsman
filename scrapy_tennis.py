#So far just for this tennis website.


from scrapy import Spider, Item, Field

STATE = 'ma'
CITY = 'boston'

class Post(Item):
	court = Field()
	address = Field()
	tel = Field()

class TennisCourtSpider(Spider):
	name, start_urls = 'tennis_courts', ['http://www.tennisround.com/tennis-courts/' + STATE + '/'+ CITY]

	def parse(self, response):
		courts = response.xpath("//div[@class='name']//a/text()")
		addresses = response.xpath("//div[@class='court-address']/text()")
		return [Post(court=courts[i].extract(), address=addresses[i*3].extract().strip(), tel=addresses[i*3+2].extract().strip()) for i in xrange(0, len(courts))]

