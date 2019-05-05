import scrapy
from newsbot.spiders.news import NewsSpider, NewsSpiderConfig
from scrapy.linkextractors import LinkExtractor

class TvZvezdaSpider(NewsSpider):
    name = "tvzvezda"
    start_urls = ["https://tvzvezda.ru/news"]
    config = NewsSpiderConfig(
        title_path='//h1/text()',
        date_path='//div[contains(@class, "date_news")]//text()',
        date_format="%H:%M %d.%m.%Y",
        text_path='//div[contains(@class, "glav_text")]//text()',
        topics_path='//meta[contains(@property, "article:section")]/@content',
        authors_path='//div[contains(@class, "autor_news")]/a/text()'
    )
    news_le = LinkExtractor(restrict_css='div.js-ajax-receiver a.news_one')

    z=0
    visited_urls = []

    def parse(self, response):
        
        if response.url not in self.visited_urls:
            for link in self.news_le.extract_links(response):
              yield scrapy.Request(url=link.url, callback=self.parse_document)
        next_pages = response.xpath('//a[contains(@class, "all_news js-ajax-call")]/@href').extract()
        next_pages=next_pages[-1]
        new_url='20/'+str(self.z)+'/?_=1542171175300'
        self.z+=20
        yield response.follow(next_pages+new_url, callback=self.parse)