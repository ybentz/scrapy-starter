# https://docs.scrapy.org/en/latest/topics/spiders.html#crawlspider
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class MyCrawlSpider(CrawlSpider):
  name = "my_crawl_spider"
  start_urls = []
  rules = ()

  def parse(self, response):
    pass
