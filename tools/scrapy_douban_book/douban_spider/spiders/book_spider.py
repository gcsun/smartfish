# -*- coding: utf-8 -*-

import scrapy
from scrapy.http import Request
from ..items import BookItem


class BookSpider(scrapy.Spider):
    name = "books"
    allowed_domanis = ["douban.com"]

    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, sdch, br",
        "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6",
        "Connection": "keep-alive",
        "Content-Type": "text/html; charset=utf-8",
        "Referer": "https://book.douban.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36",
    }

    def start_requests(self):
        return [Request('https://book.douban.com/tag/?icn=index-nav', headers=self.headers)]

    def parse_tag_page(self, response):
        book_list = response.css('li.subject-item')
        for book_item in book_list:
            item = BookItem()
            item['name'] = book_item.css(
                'div.info h2 a::text').extract_first().strip()
            # print(item['name'])
            yield item
        next_page = response.css(
            'div.paginator span.next a::attr(href)').extract_first().strip()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield Request(next_page, callback=self.parse_tag_page, headers=self.headers)

    def parse(self, response):
        tables = response.css('table.tagCol')
        for tab in tables:
            tags = tab.css('a')
            for tag in tags:
                tag_url = tag.css('a::attr(href)').extract_first().strip()
                tag_page = response.urljoin(tag_url)
                yield Request(tag_page, callback=self.parse_tag_page, headers=self.headers)
