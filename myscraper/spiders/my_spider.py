# https://docs.scrapy.org/en/latest/topics/spiders.html
from scrapy import Spider

from myscraper.items import Page, Product

class MySpider(Spider):
  name = 'my_spider'
  start_urls = ['https://www.nytimes.com/wirecutter/reviews/best-android-phone/']

  def parse(self, response):
    title = response.css('h1').get()
    update_date = response.css("time::attr(datetime)").get()
    products = self.parse_products(response)
    yield Page(title=title, update_date=update_date, products=products)

  def parse_products(self, response):
    products = []
    boxes = response.css('._587a1491')
    for box in boxes:
      name = box.css('.product-link::attr(title)').get()
      label = box.css('[data-scp="callout_label"]').get()
      buy_urls = [box.css('a[target="_blank"]::attr(href)').getall()]
      images = response.css('img[itemprop="image"]::attr(src)').get()
      product = Product(name=name, label=label, buy_urls=buy_urls, images=images)
      products.append(product)
    return products
