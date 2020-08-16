# https://docs.scrapy.org/en/latest/topics/spiders.html#crawlspider
# https://docs.scrapy.org/en/latest/topics/spiders.html#sitemapspider
from scrapy.spiders import SitemapSpider, CrawlSpider

class MySitemapSpider(SitemapSpider):
  name = "my_sitemap_spider"
  start_urls = []
  # sitemap_rules = []
  # sitemap_follow = []

  def parse(self, response):
    pass
