#!/usr/bin/python  
# -*- coding:utf-8 -*- 

from scrapy.spider import BaseSpider 
from scrapy.selector import HtmlXPathSelector
from scrmusic.items import XiamiItem
from scrapy.http import Request
cnt = 4
class DmozSpider(BaseSpider):
    name = "xiami"
    allowed_domains = ["xiami.com"]
    #设置爬取速度
    #download_delay = 1
    start_urls = [
        # 第一个网页地址
        #"http://www.xiami.com/space/charts-recent/u/40753994?spm=a1z1s.6928797.1561534497.9.itdx5s",
        "http://www.xiami.com/space/charts-recent/u/5447372?spm=a1z1s.6928793.1561534497.9.LVnEOi",
        "http://www.xiami.com/space/charts-recent/u/5447372/page/2",
        "http://www.xiami.com/space/charts-recent/u/5447372/page/3",
        "http://www.xiami.com/space/charts-recent/u/5447372/page/4",
        "http://www.xiami.com/space/charts-recent/u/5447372/page/5",
        "http://www.xiami.com/space/charts-recent/u/5447372/page/6",
        "http://www.xiami.com/space/charts-recent/u/5447372/page/7",
        "http://www.xiami.com/space/charts-recent/u/5447372/page/8",
        "http://www.xiami.com/space/charts-recent/u/5447372/page/9",
        "http://www.xiami.com/space/charts-recent/u/5447372/page/10",
        "http://www.xiami.com/space/charts-recent/u/5447372/page/11",
        "http://www.xiami.com/space/charts-recent/u/5447372/page/12",
        "http://www.xiami.com/space/charts-recent/u/5447372/page/13",
        "http://www.xiami.com/space/charts-recent/u/5447372/page/14",
        "http://www.xiami.com/space/charts-recent/u/5447372/page/15",
        "http://www.xiami.com/space/charts-recent/u/5447372/page/16",
        "http://www.xiami.com/space/charts-recent/u/5447372/page/17",
        "http://www.xiami.com/space/charts-recent/u/5447372/page/18",
        "http://www.xiami.com/space/charts-recent/u/5447372/page/19",
    ]
    """
    rules = (
        Rule(SgmlLinkExtractor(allow=r'list', tags = 'a'),
            callback = 'parse'),
    )"""
    #cnt = 10
    def parse(self, response):
        global cnt
        hxs = HtmlXPathSelector(response)
        sites = hxs.x('//table/tbody')
        items = []
        # 标记是哪个用户
        user = hxs.x('//head/title/text()').extract()[0][:-7].encode('utf-8')
        # 标记用户总共有多少条收听记录
        sum = hxs.x('//span').extract()[-3].encode('utf-8').split('共')[1].split('条')[0]
        currentPage = hxs.x('//span').extract()[-3].encode('utf-8').split('第')[1].split('页')[0]

        #for site in sites:
        if int(currentPage) <= int(sum) / 50:
            for i in range(1, 50):
                    item = XiamiItem()
                    item['user'] = user
                    item['song'] = sites.x('tr[' + str(i) + ']/td[2]/a').extract()[0].split('\"')[3].encode('utf-8')
                    print '_______________' + item['song']
                    item['artist'] = sites.x('tr[' + str(i) + ']/td[2]/a/text()').extract()[1].encode('utf-8')
                    print '+++++++++++++++' + item['artist']
                    items.append(item)
                    #yield item
            return items
        #yield items
        """ 
        if cnt < 10:
            urls = hxs.x('//div[@class="all_page"]/a/@href').extract()
            print urls
            cnt = cnt + 1
            #for url in urls:
            link = 'http://www.xiami.com/space/charts-recent/u/5447372/page/' + str(cnt) #+ urls[-1]#.split('/page/')[0] + '/page/' + "2"
            print "+++++++++++++" + link
            req = Request(url = link, meta = {
                                  'dont_redirect': True,
                                  'handle_httpstatus_list': [302]
                              
            }, callback=self.parse)
            yield req
        """
