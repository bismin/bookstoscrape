# -*- coding: utf-8 -*-
import scrapy


class BookSpider(scrapy.Spider):
    name = 'book'
    allowed_domains = ['books.toscrape.com/']
    start_urls = ['http://books.toscrape.com//']

    def parse(self, response):
    	category=response.xpath('//div[@class="page-header action"]/h1/text()').extract_first()
    	jobs=response.xpath('//li/article')
    	for job in jobs:
    			title=job.xpath('h3/a/text()').extract_first('')
    			rating=job.xpath('p/@class').extract_first('')
    			price=job.xpath('div/p/text()').extract_first('')
    			stock=job.xpath('div/p[@class="instock availability"]/text()').extract()
    			rating = rating.replace('star-rating ','')
    			stock = stock[1].strip() if stock else ''
    			yield{'title':title,'rating':rating,'price':price,'stock':stock,'category':category}
