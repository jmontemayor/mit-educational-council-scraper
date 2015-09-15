# -*- coding: utf-8 -*-
from scrapy.crawler import CrawlerProcess
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
import scrapy


class LoginSpider(scrapy.Spider):
    name = 'mitec'
    start_urls = ['https://alumsso.mit.edu/cas/login']

    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formdata={'username': 'jam1', 'password': ''},
            callback=self.after_login
        )

    def after_login(self, response):
        # check login succeed before going on
        if "The username and/or password you provided are incorrect" in response.body:
            self.logger.error("Login failed")
            return

        # continue scraping with authenticated session...
        # https://stargate.mit.edu/ectrackweb/member/resources/rcvc/stats.mit

        else:
            return Request(url="https://stargate.mit.edu/ectrackweb/member/resources/rcvc/rcvc.mit",
                           callback=self.parse_page)

    def parse_page(self, response):
        hxs = HtmlXPathSelector(response)
        links = hxs.select('//@href')

        for link in links:
            # yield Request(url=link, callback=self.parse_page)
            # yield {'url': link}
            self.logger.info(link)

def boo():
    process = CrawlerProcess({'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'})
    process.crawl(LoginSpider)
    process.start()
    return
