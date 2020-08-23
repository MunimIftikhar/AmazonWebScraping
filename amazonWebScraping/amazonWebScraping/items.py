# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonwebscrapingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    product_title = scrapy.Field()
    product_url = scrapy.Field()
    product_ratings = scrapy.Field()
    product_reviews = scrapy.Field()
    product_price = scrapy.Field()
    product_image = scrapy.Field()
    pass
