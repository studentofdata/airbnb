import logging
import scrapy
from scrapy.spiders import CrawlSpider, BaseSpider, Rule
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
from airbnb.items import AirbnbItem


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class airbnbCollector(CrawlSpider):

	name = 'airbnb'
	start_urls = ["https://www.airbnb.com/s/Monterey--CA--United-States"]

	rules = (
		
		Rule(LinkExtractor(allow = ("/s/Monterey--CA--United-States")), callback = "parse_pages", follow = True),
		
		Rule(LinkExtractor(allow = ("/rooms")), callback = "parse_locations", follow = True)

			)


	def parse_pages(self, response):
		pass


	def parse_locations(self, response):
		sel = Selector(response)

		property_site = AirbnbItem()

		property_site['R_Hostname']      = sel.xpath('//a[contains(@href, "#host-profile")]/text()').extract()[1]
		property_site['R_Hostprofile']   = sel.xpath('//div[contains(@data-reactid, ".agcwfvnqbk.2.0.0.0.2.1")]/a/@href').extract()
		property_site['R_Listname']	     = sel.xpath('//h1[@id = "listing_name"]/text()').extract()
		property_site['R_Reviews']	     = sel.xpath('//span[@itemprop = "reviewCount"]/text()').extract()


		property_site['S_Accommodates'] = sel.xpath('//strong[contains(@data-reactid, "Accommodates=2.2")]/text()').extract()
		property_site['S_Bedrooms']	   = sel.xpath('//strong[contains(@data-reactid, "Bedrooms=2.2")]/text()').extract()
		property_site['S_Bathrooms']   = sel.xpath('//strong[contains(@data-reactid, "Bathrooms=2.2")]/text()').extract()
		property_site['S_Numbeds']     = sel.xpath('//strong[contains(@data-reactid, "Beds=2.2")]/text()').extract()
		property_site['S_Bedtype']	   = sel.xpath('//strong[contains(@data-reactid, "Bed type=2.2")]/text()').extract()
		property_site['S_Checkin']	   = sel.xpath('//strong[contains(@data-reactid, "Check Out=2.2")]/text()').extract()
		property_site['S_Checkout']	   = sel.xpath('//strong[contains(@data-reactid, "Check In=2.2")]/text()').extract()


		property_site['A_Availability'] = sel.xpath('//div[@class = "col-md-6"]/strong/text()').extract()
		#Why the fuck does this work?
		property_site['R_Value']	   = sel.xpath('//div[@class = "col-sm-8"]/div/span/text()').extract()
		#Not a fan of the following xpath, fix later
		property_site['R_Roomtype']	   = sel.xpath('//div[@class = "col-sm-3"]/text()').extract()[0]

		property_site['A_Cleaningfee'] = sel.xpath('//strong[contains(@data-reactid, "Cleaning Fee=2.2")]/text()').extract()


		return property_site
