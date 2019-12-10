# -*- coding: utf-8 -*-
import scrapy
from shiyanlou.items import UserItem

class UsersSpider(scrapy.Spider):
    name = 'users'
    allowed_domains = ['shiyanlou.com']

    @property
    def start_urls(self):
        """
        实验楼注册的用户数目前大约六十几万, 为了爬虫的效率,
        取 id 在 524,8000~525,000 之间的新用户,
        每间隔 10 取一个, 最后大概爬取 20 个用户的数据
        """
        url_tmp = 'https://www.shiyanlou.com/users/{}'
        return (url_tmp.format(i) for i in range(525000,524800, -10))

    def parse(self, response):
        item = UserItem({
            'name': response.css('div.user-meta span::text').extract()[0].strip(),
            'level': response.css('div.user-meta span::text').extract()[1].strip(),
            'status': response.css('div.user-status span::text').extract_first(default='无').strip(),
            'school_job': response.xpath('//div[@class="user-status"]/span[2]/text()').extract_first(default='无').strip(),
            'join_date': response.css('span.user-join-date::text').extract_first().strip(),
            'learn_courses_num': response.css('span.tab-item::text').re_first('\D+(\d+)\D+')
            })
        if len(response.css('div.user-avatar img').extract()) == 2:
            item['is_vip'] = True

        yield item
