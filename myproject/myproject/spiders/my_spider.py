import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class MySpider(CrawlSpider):
    name = 'my_spider'
    allowed_domains = ['xcelore.com']
    start_urls = ['https://xcelore.com/']

    rules = (
        Rule(LinkExtractor(), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        self.log(f'Visited: {response.url}')


        page_title = response.css('title::text').get()
        page_content = response.css('body').get()


        paragraphs = response.css('p::text').getall()
        content = ' '.join(paragraphs)


        yield {
            'url': response.url,
            'title': page_title,
            'content': content
        }
