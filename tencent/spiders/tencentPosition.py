# -*- coding: utf-8 -*-
import scrapy
from tencent.items import TencentItem


class TencentpositionSpider(scrapy.Spider):
    name = 'tencentPosition'
    allowed_domains = ["tencent.com"]

    url = "http://hr.tencent.com/position.php?&start="
    offset = 0

    start_urls = [url + str(offset)]

    def parse(self, response):

        #print(response.body)

        for each in response.xpath("//tr[@class='even'] | //tr[@class='odd']"):
            item = TencentItem()

            # # 姓名
            # item['positionname'] = each.xpath("./td[1]/a/text()").extract()[0]
            # # 链接
            # item['positionlink'] = each.xpath("./td[1]/a/@href").extract()[0]
            # # 职位列别
            # item['positionType'] = each.xpath("./td[2]/text()").extract()[0]
            #
            # # 招聘人数
            # item['peopleNum'] = each.xpath("./td[3]/text()").extract()[0]
            # # 工作地点
            # item['workLocation'] = each.xpath("./td[4]/text()").extract()[0]
            # # 发布时间
            # item['publishTime'] = each.xpath("./td[5]/text()").extract()[0]

            item['positionname'] = each.xpath("./td[1]/a/text()").extract()[0]
            # 详情连接
            item['positionlink'] = each.xpath("./td[1]/a/@href").extract()[0]
            # 职位类别

            try:

                item['positionType'] = each.xpath("./td[2]/text()").extract()[0]

            except IndexError:

                item['positionType'] = None




            #tem['positionType'] = each.xpath("./td[2]/text()").extract()[0]
            # 招聘人数
            item['peopleNum'] =  each.xpath("./td[3]/text()").extract()[0]
            # 工作地点
            item['workLocation'] = each.xpath("./td[4]/text()").extract()[0]
            # 发布时间
            item['publishTime'] = each.xpath("./td[5]/text()").extract()[0]








            yield item

        if self.offset < 50:

            self.offset += 10
        #
        # else:
        #     break
        #每次处理我那一页数据之后，重新发起请求

        yield scrapy.Request(self.url + str(self.offset), callback=self.parse)





