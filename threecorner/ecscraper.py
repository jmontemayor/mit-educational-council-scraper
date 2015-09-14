# -*- coding: utf-8 -*-
from scrapy.crawler import CrawlerProcess
import scrapy


class LoginSpider(scrapy.Spider):
    name = 'mitec'
    start_urls = ['https://alumsso.mit.edu/cas/login?service=https%3A%2F%2Falum.mit.edu%2Faccount%2Fj_spring_cas_security_check']

    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formdata={'username': 'jam1', 'password': ''},
            callback=self.after_login
        )

    def after_login(self, response):
        # check login succeed before going on
        if "authentication failed" in response.body:
            self.logger.error("Login failed")
            return

        # continue scraping with authenticated session...
        # https://stargate.mit.edu/ectrackweb/member/resources/rcvc/stats.mit
        def make_requests_from_url(self, url):
            url = "https://stargate.mit.edu/ectrackweb/member/resources/rcvc/stats.mit"


def boo():
    process = CrawlerProcess({'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'})
    process.crawl(LoginSpider)
    process.start()
    return
