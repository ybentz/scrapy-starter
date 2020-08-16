# https://docs.scrapy.org/en/latest/topics/spiders.html
from scrapy import Spider

class MySpider(Spider):
  name = "my_spider"
  start_urls = []

  def parse(self, response):
    pass
