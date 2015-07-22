#!/usr/bin/env python
# -*- coding: utf-8 -*-
import scrapy
import sys, re, json
from BeautifulSoup import BeautifulSoup
from scrapy.spiders import Spider
from scrapy.selector import Selector
from my_scrapy.items import Tieba_post_item

# reload(sys)
# sys.setdaulftencoding('utf-8')

rep_num_for_good = 100
Tieba_admin_url = "http://tieba.baidu.com/"


class Dmozspider(Spider):

    """docstring for Dmozspider"""
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://tieba.baidu.com/f?kw=%C3%C0%BE%E7&fr=ala0&loc=rec",
        # "http://tieba.baidu.com/f?kw=android&ie=utf-8"
    ]

    def parse(self, response):

        post_items = []
        # use BeautifulSoup
        # soup = BeautifulSoup(response.body)
        # open("meuju.html", 'wb').write(soup.prettify())
        # titles =''
        # #get each tieba article in top view
        # lis = soup.findAll('li', attrs = {'class':'j_thread_list clearfix'})
        # print len(lis)
        # for a in lis:
        #     #get reply number
        #     rep_num = int(a.findAll('div', attrs = {'class':'threadlist_rep_num'})[0].renderContents())
        #     if rep_num > rep_num_for_good:
        #         #get article title
        #         title = a.findAll('a', attrs = {'class':'j_th_tit'})[0].renderContents()
        #         titles += '['+ str(rep_num) + ']' + title + '\r'
        #         open("meuju", 'wb').write(titles)

        # xpath
        sel = response.xpath('//li[@class="j_thread_list clearfix"]')
        print len(sel)
        titles = ''
        for li in sel:
            post = Tieba_post_item()
            data_field = json.loads(li.xpath('.//@data-field').extract()[0])
            # print data_field
            post['rep_num'] = data_field['reply_num']
            if post['rep_num'] > rep_num_for_good:
                # #tag a with clss include j_th_tit
                # title = li.xpath('.//a[contains(@class,"j_th_tit")]/text()').extract()
                #tag a class name is j_th_tit
                post['url_link'] = Tieba_admin_url + 'p/' + str(data_field['id'])
                post['title'] = li.xpath('.//a[@class="j_th_tit"]/text()').extract()[0]
                # title = li.xpath('/div[1]div/div/div/a/text()').extract()
                post['body'] =  li.xpath('.//div[@class="threadlist_abs threadlist_abs_onlyline"]/text()').extract()[0]
                # open("meuju", 'wb').write(post['title'])
                post_items.append(post)
        return post_items



if __name__ == "__main__":
    a = u'\u4f60\u89c9\u5f97\u6211\u597d\u770b\u4f60\u5c31\u591a\u770b\u4e24\u773c\uff0c\u4e0d\u597d\u770b\u5c31\u522b\u770b\u5457'
    print a.encode('utf-8')
    print sys.getdefaultencoding()
    with open('2.html', 'rw') as f:
        doc = f.read()
