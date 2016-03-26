# -*- coding:utf8 -*-
import urllib2, os, os.path, urllib, random
import re,requests
from bs4 import BeautifulSoup

my_headers = [
'Mozilla/5.0 (Windows NT 5.2) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.122 Safari/534.30',
'Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0',
'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET4.0E; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C)',
'Opera/9.80 (Windows NT 5.1; U; zh-cn) Presto/2.9.168 Version/11.50',
'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/533.21.1 (KHTML, like Gecko) Version/5.0.5 Safari/533.21.1',
'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022; .NET4.0E; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C)']
header={"User-Agent":random.choice(my_headers)}
#req=urllib2.Request(url, headers=header)
#html=urllib2.urlopen(req).read()
prog = re.compile(r'ag\_ele\_v.*')
s = prog.findall('http://tieba.baidu.com/p/3140419486#!/l/p1')
#soup=BeautifulSoup('test.html','lxml')
#s = soup.find_all('div',class_="ag_ele ag_ele_v")
#s = requests.session()
#htmlpage = s.get('http://huaban.com/favorite/beauty/').content
#prog = re.compile(r'app\.page\["pins"\].*')
#appPins = prog.findall(htmlpage)
print s