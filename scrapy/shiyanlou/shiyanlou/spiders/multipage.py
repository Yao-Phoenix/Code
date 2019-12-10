# -*- coding: utf-8 -*-
import scrapy
from shiyanlou.items import MultipageCourseItem

class MultipageSpider(scrapy.Spider):
    name = 'multipage'
    
    @property
    def start_urls(self):
        url = ['https://www.shiyanlou.com/courses/']
        return url

    def parse(self, response):
        for course in response.css('div.col-md-3'):
            item = MultipageCourseItem(
                    name = course.css('h6.course-name::text').extract_first().strip(),
                    image = course.css('img.cover-image::attr(src)').extract_first()
                    )
            course_url = course.css('a::attr(href)').extract_first()
            full_course_url = response.urljoin(course_url)
            request = scrapy.Request(full_course_url, self.parse_author)
            request.meta['item'] = item
            yield request

    def parse_author(self, response):
        item = response.meta['item']
        item['author'] = response.css('p.teacher-info span::text').extract_first()
        yield item
