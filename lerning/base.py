#!/usr/bin/ env python
# coding:utf-8

import urllib
import urllib2
import cookielib
from BeautifulSoup import *


web_site = 'https://kbits-cnn.labcollab.net:9418/project/full_ford_main_dev'

class Login(object):

    def __init__(self):
        self.name = ''
        self.passwprd = ''
        self.domain = ''
        self.cj = cookielib.LWPCookieJar()
        self.opener = urllib2.build_opener(
            urllib2.HTTPCookieProcessor(self.cj))
        urllib2.install_opener(self.opener)

    def setLoginInfo(self, username, password, domain):
        self.name = username
        self.pwd = password
        self.domain = domain

    def login(self, loginurl):
        loginparams = {
            'domain': self.domain, 'username': self.name, 'password': self.pwd}
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:37.0) Gecko/20100101 Firefox/37.0'}
        req = urllib2.Request(
            loginurl, urllib.urlencode(loginparams), headers=headers)
        response = urllib2.urlopen(req)
        self.operate = self.opener.open(req)
        thePage = response.read()


if __name__ == "__main__":
    userlogin = Login()
    username = 'ext-huaqin-liuzhigang'
    password = 'ASDqwe~123'
    domain = "kbits-cnn.labcollab.net:9418"
    userlogin.setLoginInfo(username, password, domain)
    userlogin.login(web_site)

# cookie = cookielib.CookieJar()
# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
# response = opener.open('http://www.baidu.com')
# for item in cookie:
# print 'Name = '+item.name
# print 'Value = '+item.value

# web_site = 'https://kbits-cnn.labcollab.net:9418/project/full_ford_main_dev'
# web_site = "https://www.baidu.com"
# req = urllib2.Request(web_site)
# response = opener.open(req)
# the_page = response.read()
# print the_page
# for item in cookie:
#                 print item

# with open('web1.html','wb') as f:
#        f.write(the_page)

# soup = BeautifulSoup(the_page)
# help(soup)
# print soup.findAll('input')
# get the real web_site, you will be redirected
# real_url = response.geturl()
# print real_url
# print response.info()
