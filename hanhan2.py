# -*- coding:utf-8 -*-
import urllib2
import time

content = urllib2.urlopen('http://blog.sina.com.cn/s/articlelist_1191258123_0_1.html').read()
url = ['']*100
filename = ['']*100
i = 0

set_local = content.find(r'<a title')
start = content.find(r'href',set_local)
end = content.find(r'html',start)
#for_filename1 = content.find(r'>',end)
#for_filename2 = content.find(r'</a',end)


while set_local != 0 and i < 100:
    url[i] = content[start+6:end+4]
	#for_filename1 = content.find(r'>',end)
	#for_filename2 = content.find('</a>',end)
	#filename[i] = content[end+4:for_filename2]
    set_local = content.find(r'<a title',end) 
    start = content.find(r'href',set_local)
    end = content.find(r'html',start)
	#for_filename1 = content.find(r'>',start)
	#filename2 = content.find(r'</a',end)
	#filename[i] = content[end+4:for_filename2]
    i += 1
else:
    print 'find finished'

j = 0
while j < 50:
	
	filename = url[j][url[j].find(r'blog_'):]
	con = urllib2.urlopen(url[j]).read()
	open (r'E:\somegit\learncrawler\hanhan\ '+filename,'w').write(con)
	print 'downloading',url[j]
	time.sleep(1)
	j += 1
else:
	print 'ok'
