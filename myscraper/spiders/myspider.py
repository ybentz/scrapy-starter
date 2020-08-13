# https://docs.scrapy.org/en/latest/topics/spiders.html
from scrapy import Spider
# https://docs.scrapy.org/en/latest/topics/spiders.html#crawlspider
# https://docs.scrapy.org/en/latest/topics/spiders.html#sitemapspider
from scrapy.spiders import SitemapSpider, CrawlSpider

class MySpider(Spider):
  name = "myspider"
  start_urls = []

  def parse(self, response):
    pass
