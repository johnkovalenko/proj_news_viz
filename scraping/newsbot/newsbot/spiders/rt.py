from newsbot.spiders.news import NewsSpider, NewsSpiderConfig
from scrapy import Request, Selector

from typing import List
from datetime import date


class RussiaTodaySpider(NewsSpider):
    name = 'rt'

    start_urls = ['https://russian.rt.com/sitemap.xml']

    config = NewsSpiderConfig(
        title_path='//h1/text()',
        date_path='//meta'
        '[contains(@name, "mediator_published_time")]/@content',
        date_format="%Y-%m-%dT%H:%M:%S",
        text_path='//div[contains(@class, "article__text")]//text()',
        topics_path='//meta'
        '[contains(@name, "mediator_theme")]/@content'
        # TO-DO: check topics_path if needed to change mediator_theme by
        # description.
    )

    def _parse_xml(self, response, main=None):
        '''Wrap parsing sitemap.xml or sub-sitemaps.
        '''
        body = response.body
        links = Selector(text=body).xpath('//loc/text()')

        for link in links.getall():
            if main:
                yield link
            else:
                yield Request(url=link,
                              callback=self.parse_document)

    def parse(self, response):
        '''Firstly, parse main sitemap.xml, which has a sub-sitemaps.

        If it is a sub_sitemap then extract articles and parse them with
        super().parse_document.
        '''
        sitemaps = self._parse_xml(response, main=True)

        for sitemap in sitemaps:
            # TO-DO: before an article checking sitemap with until_date.
            yield Request(url=sitemap,
                          callback=self._parse_xml)

    def _fix_syntax(self, sample: List[str], idx_split: int) -> List[str]:
        '''Fix timestamp syntax, droping timezone postfix.
        '''
        sample = [sample[0][:idx_split]]
        return sample

    def _get_date(self, lst: List[str]):
        '''Convert list into date obj.
        '''
        y, m, d = [int(num) for num in lst]
        return date(y, m, d)

    def parse_document(self, response):
        '''Finally, parse each article.
        '''
        for item in super().parse_document(response):

            # Try to drop timezone postfix.
            try:
                item['date'] = self._fix_syntax(item['date'], -6)
            except KeyError:
                print('Error. No date value.')
            else:
                _article_time = \
                    self._get_date(item['date'][0][:10].split('-'))

                if _article_time >= self.until_date:
                    yield item
