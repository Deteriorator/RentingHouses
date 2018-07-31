# -*- coding: utf-8 -*-
import scrapy


class ZufangSpider(scrapy.Spider):
    name = 'Zufang'
    allowed_domains = ['su.zu.anjuke.com']
    start_urls = ['http://su.zu.anjuke.com/']

    def parse(self, response):
        pass
