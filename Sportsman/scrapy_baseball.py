#So far just for this tennis website.


from scrapy import Spider, Item, Field

CITY_LIST = ['Los_Angeles', 'Oakland,_California', 'San_Diego', 'San_Francisco', 'Denver', 'Washington,_D.C.', 'Miami', 'Tampa_Bay,_Florida', 'Atlanta', 'Chicago', 
			'Indianapolis', 'Louisville,_Kentucky', 'Baltimore', 'Boston', 'Detroit', 'Minneapolis-Saint_Paul,_Minnesota', 'Kansas_City,_Missouri', 'St._Louis', 
			'Newark,_New_Jersey', 'Buffalo,_New_York', 'New_York_City', 'Cincinnati', 'Cleveland', 'Toledo,_Ohio', 'Portland,_Oregon', 'Philadelphia', 'Pittsburgh',
			'the_Dallas-Fort_Worth_Metroplex', 'Houston', 'San_Antonio', 'Milwaukee', 'Toronto', 'Montreal']

class Post(Item):
	name = Field()
	location = Field()

class BaseballCourtSpider(Spider):
	name, start_urls = 'baseball_courts', ['http://en.wikipedia.org/wiki/List_of_baseball_parks_in_' + CITY_LIST[0]]

	def parse(self, response):
		name = response.xpath("//dt/text()")
		location = response.xpath("//dd[contains(., 'Location')]/text()")
		return [Post(name=name[i].extract().strip(), location=location[i].extract().strip()) for i in xrange(0, len(location))]

