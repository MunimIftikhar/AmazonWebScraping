import scrapy
import re
import json
import os
from pathlib import Path
from ..items import AmazonwebscrapingItem

class amazonSpider(scrapy.Spider):

    #Input the product name from user and parse it to generate a url
    product = input('Please enter product name: ')  # Enter product name here
    if ' ' in product:
        p = product.split(' ')
        print(p)
        product = p[0]
        for i in range(1, len(p)):
            product += '+'
            product += p[i]

    name = 'amazon'
    page_number=2 #used to extract from other pages

    #url according to the given product
    start_urls = ['https://www.amazon.com/s?k=' + product]

    def start_requests(self): #making a start request
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        items = AmazonwebscrapingItem()
        # extracting the data from website
        all_div_products = response.css('div[data-component-type="s-search-result"]')

        for products in all_div_products:
            product_title= products.css('span.a-text-normal').css('::text').extract()
            product_url= products.css('a.a-link-normal.a-text-normal').css('::attr(href)').extract()
            product_ratings = products.css('div.a-row.a-size-small span:nth-of-type(1)').css('::attr(aria-label)').extract()
            product_reviews=products.css('div.a-row.a-size-small span:nth-of-type(2)').css('::attr(aria-label)').extract()
            product_price=products.css('span.a-price:nth-of-type(1) span.a-offscreen').css('::text').extract()
            product_image=products.css('.s-image').css('::attr(src)').extract()

            if product_price is None:
                product_price = 'not mentioned'
            #saving the extracted data in items
            items["product_title"] = product_title
            items["product_url"] = product_url
            items["product_ratings"] = product_ratings
            items["product_reviews"] = product_reviews
            items["product_price"] = product_price
            items["product_image"] = product_image

            yield items
            #extract data from available pages of the given product
            next_page = 'https://www.amazon.com/s?k=' + self.product + '&page=' + str(self.page_number)
            self.page_number += 1
            yield response.follow(next_page, callback=self.parse)
