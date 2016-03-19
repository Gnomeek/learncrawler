import urllib
import urllib2
from bs4 import BeautifulSoup

values = {'username':'617243899@qq.com','password':'501826'}
data = urllib.urlencode(values)
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64)'
headers = {'User-Agent':user_agent,'Referer':'http://www.zhihu.com/articles'}
url = 'http://user.qzone.qq.com/617243899'
request = urllib2.Request(url)
response = urllib2.urlopen(request)
obj = response.read()
zhihu = open('kongjian.html','w')
zhihu.write(obj)
#zhihu.truncate()
zhihu.close()
