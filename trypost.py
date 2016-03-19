import urllib
import urllib2

url = 'https://passport.csdn.net/account/login'
values = {'username':'15140327802','password':'501826'}
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64)'
data = urllib.urlencode(values)
headers = {'User_agent':user_agent}
#geturl = url +'?' + data
request = urllib2.Request(url,data,headers)
response = urllib2.urlopen(request)
file = open('csdn.html','w')
obj = response.read()
file.write(obj)
#print geturl
#failed