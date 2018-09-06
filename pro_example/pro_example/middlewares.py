# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html


import re
import base64
import random
import logging
import urllib.parse as urlparse
import threading

from .uapool import ua_pool,ua_pool_m
from scrapy import signals
from scrapy.conf import settings
from scrapy.http import HtmlResponse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class ProExampleSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class ProExampleDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)



class RandomHeaders(object):
    def process_request(self, request, spider):
        request.headers['Host'] = urlparse.urlparse(request.url).netloc


        request.headers['User-Agent'] = random.choice(ua_pool_m)

        request.headers['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
        request.headers['Accept-Language'] = 'zh-CN,zh;q=0.8,en;q=0.6'
        request.headers['Accept-Encoding'] = 'deflate'

        # request.headers['Origin'] = 'http://www.baidu.com'
        # request.headers['Connection'] = 'keep-alive'
        # request.headers['Cookie'] = 'cookie'
        # request.headers['Cache-Control'] = 'max-age=0'
        # request.headers['Upgrade-Insecure-Requests'] = '1'
        # request.headers['If-Modified-Since'] = time.strftime(u'%a, %d %b %Y %H:%M:%S GMT', time.gmtime())
        # request.headers['Content-Type'] = 'application/x-www-form-urlencoded; charset=UTF-8'
        # request.headers['X-Requested-With'] = 'XMLHttpRequest'


class RandomIP(object):
    def process_request(self, request, spider):
        # 例：request.meta['proxy'] = urlparse.urlparse(request.url).scheme + '://' + '127.0.0.1:8888'
        request.meta['proxy'] = urlparse.urlparse(request.url).scheme + '://'



