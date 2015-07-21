#!/usr/bin/ env python
# coding:utf-8

import urllib
import urllib2
import cookielib
from BeautifulSoup import *


s = "你好"  # 整个文件是UTF-8编码，所以这里的字符串也是UTF-8
u = s.decode("utf-8")  # 将utf-8的str转换为unicode
g = u.encode('GBK')  # 将unicode转换为str，编码为GBK

web_site = "http://index.baidu.com/?tpl=trend&word=%B1%B1%BE%A9"
tokenVal = "51539d037e917539102f5f0878268d2e"
username = "ganggegedahuB"
password = "liu7536308"

#------------------------------------------------------------------------------
#设置一个cookie处理器，它负责从服务器下载cookie到本地，并且在发送请求时带上本地的cookie
cj = cookielib.LWPCookieJar()
cookie_support = urllib2.HTTPCookieProcessor(cj)
opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
urllib2.install_opener(opener)

#------------------------------------------------------------------------------
# just for print delimiter
def printDelimiter():
    print '-'*80

def login_baidu_index():

    #打开登录主页面（他的目的是从页面下载cookie，这样我们在再送post数据时就有cookie了，否则发送不成功）  
    h = urllib2.urlopen(web_site)

    staticpage = "http://index.baidu.com/static/v3Jump.htm"
    baiduMainLoginUrl = "https://passport.baidu.com/v2/api/?login"
    postDict = {
            #'ppui_logintime': "",
            'charset'       : "gbk",
            #'codestring'    : "",
            'token'         : tokenVal,
            'isPhone'       : "false",
            'index'         : "0",
            'u'             : "http://index.baidu.com/?tpl=trend&word=%B1%B1%BE%A9%CA%B1%BC%E4",
            #'safeflg'       : "0",
            'staticpage'    : staticpage, #http%3A%2F%2Fwww.baidu.com%2Fcache%2Fuser%2Fhtml%2Fjump.html
            'loginType'     : "1",
            'tpl'           : "index",
            'callback'      : "parent.bd__pcbs__wbf8zj",
            'username'      : username,
            'password'      : password,
            #'verifycode'    : "",
            'mem_pass'      : "on",
    }
    postData = urllib.urlencode(postDict)


    req = urllib2.Request(web_site, postData)
        # in most case, for do POST request, the content-type, is application/x-www-form-urlencoded
    req.add_header('Content-Type', "application/x-www-form-urlencoded")
    print req.POST
    return urllib2.urlopen(req)

html = login_baidu_index().read()

# response = urllib2.urlopen(web_site)
# html = response.read()
# print response.info()

with open('web1.html','wb') as f:
       f.write(html)