# -*- coding: utf-8 -*-
import scrapy


class BookSpider(scrapy.Spider):
    name = 'book'
    allowed_domains = ['books.toscrape.com/']
    start_urls = ['http://books.toscrape.com//']

    def parse(self, response):
    	category=response.xpath('//div[@class="page-header action"]/h1/text()').extract_first()
    	jobs=response.xpath('//li[@class="col-xs-6 col-sm-4 col-md-3 col-lg-3"]/article[@class="product_pod"]')
    	for job in jobs:
    			title=job.xpath('h3/a/text()').extract_first()
    			rating=job.xpath('p/@class').extract_first()
    			price=job.xpath('div[@class="product_price"]/p[@class="price_color"]/text()').extract_first()
    			stock=job.xpath('div[@class="product_price"]/p[@class="instock availability"]/text()').extract()
    			yield{'title':title,'rating':rating,'price':price,'stock':stock,'category':category}
