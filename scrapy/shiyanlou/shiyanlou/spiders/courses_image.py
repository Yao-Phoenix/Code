#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import scrapy
from shiyanlou.items import CourseImageItem

class CoursesImageSpider(scrapy.Spider):
    name = 'courses_image'

    @property
    def start_urls(self):
        url = ['https://www.shiyanlou.com/courses/']
        return url

    def parse(self, response):
        item = CourseImageItem()
        # 解析图片链接到 item
        item['image_urls'] = response.xpath('//img[@class="cover-image"]/@src').extract()
        yield item
