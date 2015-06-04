# -*- coding: utf-8 -*-
import urllib2




# 创建一个密码管理者
# password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()

# 添加用户名和密码

# top_level_url = "https://kbits-cnn.labcollab.net:9418/login"

# 如果知道 realm, 我们可以使用他代替 ``None``.
# # password_mgr.add_password(None, top_level_url, username, password)
# username = 'ext-huaqin-liuzhigang'
# password = 'ASDqwe~123'
# password_mgr.add_password(None, top_level_url, username, password)

# 创建了一个新的handler
# handler = urllib2.HTTPBasicAuthHandler(password_mgr)

# 创建 "opener" (OpenerDirector 实例)
# opener = urllib2.build_opener(handler)
httpHandler = urllib2.HTTPHandler(debuglevel=1)
httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
opener = urllib2.build_opener(httpHandler, httpsHandler)
# a_url = 'https://kbits-cnn.labcollab.net:9418/project/full_ford_main_dev'

# 使用 opener 获取一个URL


# 安装 opener.
# 现在所有调用 urllib2.urlopen 将用我们的 opener.
urllib2.install_opener(opener)

web_site = 'https://kbits-cnn.labcollab.net:9418/project/full_ford_main_dev'
req = urllib2.Request(web_site)
response = urllib2.urlopen(req)
the_page = response.read()

#get the real web_site, you will be redirected
real_url = response.geturl()
print real_url
print response.info()