# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class Page(scrapy.Item):
    products = scrapy.Field()
    title = scrapy.Field()
    update_date = scrapy.Field()

class Product(scrapy.Item):
    name = scrapy.Field()
    label = scrapy.Field()
    buy_urls = scrapy.Field()
    images = scrapy.Field()
