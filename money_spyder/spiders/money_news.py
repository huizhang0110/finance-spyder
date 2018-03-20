# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request, HtmlResponse
from urllib import parse
from money_spyder.items import MoneySpyderItem
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import time
import re


class MoneyNewsSpider(scrapy.Spider):
    name = 'money_news'
    allowed_domains = ['http://roll.finance.sina.com.cn/blog/blogarticle']
    start_urls = ['http://roll.finance.sina.com.cn/blog/blogarticle/cjbk-qyj/index_1.shtml']


    def parse(self, response):
        post_urls = response.xpath('//ul[@class="list_009"]//li/a[1]/@href').extract()
        for post_url in post_urls:
            post_url = parse.urljoin(response.url, post_url)
            time.sleep(1)
            print(post_url)
            yield Request(url=post_url, callback=self.parse_content, dont_filter=True)

        next_page_url = response.xpath('//span[@class="pagebox_next"]/a/@href')[0].extract()
        if next_page_url:
            next_page_url = parse.urljoin(self.allowed_domains[0], next_page_url)
            yield Request(url=next_page_url, callback=self.parse, dont_filter=True)

    def parse_content(self, response):
        item = MoneySpyderItem()
        item['url'] = response.url
        if response.url.endswith('shtml'):
            item['content'] = response.xpath('//*[@id="artibody"]//p/text()').extract()
        else:
            item['content'] = response.xpath('//*[@id="sina_keyword_ad_area2"]//p/text()|//*[@id="sina_keyword_ad_area2"]//p//span/text()').extract()
        yield item
