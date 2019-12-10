# -*- coding: utf-8 -*-
import scrapy
from shiyanlou.items import CourseItem

class CoursesSpider(scrapy.Spider):
    name = 'courses'
    
    @property
    def start_urls(self):
        url_list = ['https://www.shiyanlou.com/courses/',
                'https://www.shiyanlou.com/courses/?page=2',
                'https://www.shiyanlou.com/courses/?page=3',]
        return url_list

    def parse(self, response):
        for course in response.css('div.col-md-3'):
            item = CourseItem({
                'name': course.css('h6::text').extract_first().strip(),
                'description': course.css('div.course-description::text').extract_first().strip(),
                'type': course.css('span.course-type::text').extract_first('免费').strip(),
                'students': course.css('span.students-count span::text').extract_first()
                })
            yield item
