#!/usr/bin/env python3
import scrapy

class ShiyanlouCoursesSpider(scrapy.Spider):
    """
    使用 scrapy 爬取页面数据需要编写一个爬虫类，更改爬虫类要继承 scrapy.Spider 类
    在爬虫类中定义要请求的网站和连接、如何从返回的网页提取数据等等
    在 scrapy 项目中可能会有多个爬虫，name 属性用于标识每个爬虫， 各个爬虫类的 name 值不能相同
    """
    name = 'shiyanlou-courses'

    '''
    # 注意此方法的方法名字是固定的，不可更改
    def start_requests(self):
        """
        此方法需要返回一个可迭代对象，迭代的元素是 scrapy.Request 对象
        可迭代对象可以是一个列表或者迭代器， 这样 scrapy 就知道有哪些网页需要爬取了
        scrapy.Request 接受一个 url 参数和一个 callback 参数
        url 指明要爬取的网页
        callback 是一个回调函数，用于处理返回的网页， 它的值通常是一个提取数据的 parse 方法
        """
    '''
    @property
    def start_urls(self):
        """
        start_urls 需要返回一个可迭代对象， 所以， 你可以把它写成一个列表、元组或者生成器， 这里用的是列表
        """

        # 课程列表页面 URL， 注意此列表中的地址可能有变动，需手动打开页面复制最新地址
        url_list = ['https://www.shiyanlou.com/courses/',
                'https://www.shiyanlou.com/courses/?page=2',
                'https://www.shiyanlou.com/courses/?page=3']
        return url_list
        '''
        # 返回一个生成器， 生成 Request 对象，生成器是可迭代对象
        for url in url_list:
            yield scrapy.Request(url=url, callback=self.parse)
        '''

    # 注意此方法的方法名字也是固定的，不可更改
    def parse(self, response):
        """
        这个方法作为 scrapy.Request 的 callback, 在里面编写提取数据的代码
        scrapy 中的下载器会下载 start_requests 中定义的每个 Request
        并且将结果封装为一个 response 对象传入这个方法
        """
        # 遍历每个课程的 div.col-md-3
        for course in response.css('div.col-md-3'):
            # 使用 css 语法对每个 course 提取数据
            yield {
                # 课程名称， 注意这里使用 strip 方法去掉字符串前后的空白字符
                # 所谓空白字符， 指的是空格、换行符、制表符
                # 下面获取 name 的写法还可以省略 h6 的类属性, 思考一下为什么可以省略
                'name': course.css('h6.course-name::text').extract_first().strip(),
                # 课程描述
                'description': course.css('div.course-description::text').extract_first().strip(),
                # 课程类型
                'type': course.css('span.course-type::text').extract_first('免费').strip(),
                # 学生人数
                'students': course.css('span.students-count span::text').extract_first()
                }
