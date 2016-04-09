import urllib
import urllib2
import random
from bs4 import BeautifulSoup

my_headers = [
    'Mozilla/5.0 (Windows NT 5.2) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.122 Safari/534.30',
    'Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET4.0E; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C)',
    'Opera/9.80 (Windows NT 5.1; U; zh-cn) Presto/2.9.168 Version/11.50',
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/533.21.1 (KHTML, like Gecko) Version/5.0.5 Safari/533.21.1',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022; .NET4.0E; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C)']
header={"User-Agent":random.choice(my_headers)}

#html=urllib2.urlopen(req).read()

url = u'http://flight.elong.com/isajax/OneWay/S?_=1460103006977&PageName=list&FlightType=OneWay&DepartC\
ity=dlc&DepartCityName=%E5%A4%A7%E8%BF%9E&DepartCityNameEn=Dalian&ArriveCity=cgo&ArriveCityName=%E9%83%\
91%E5%B7%9E&ArriveCityNameEn=Zhengzhou&DepartDate=2016%2F4%2F8+0%3A00&BackDate=2016%2F4%2F11+0%3A00&Day\
Count=0&BackDayCount=3&SeatLevel=Y&IssueCity=dlc&OrderBy=Price&OrderFromId=50793&AirCorp=0&ElongMemberL\
evel=Common&viewpath=~%2Fviews%2FList%2Foneway.aspx'
req=urllib2.Request(url, headers=header)
response = urllib2.urlopen(req)
obj = response.read()
test = open('yilong2.html','w')
test.write(obj)
#zhihu.truncate()
test.close()
